import customtkinter as ctK     # Importing Custom Tkinter as ctK
import threading                # Purpose of Threading is to run different parts of the program simultaneously.
import socket                   # Socket Library is used to connect to a specified IP Address, and access it's ports.       
import time                     # Used to represent time in a code.
from IPy import IP              # A Python Module used to handle IPv4 and IPv6 Addresses and networks.           
from datetime import datetime   # Python Library consists of a combination of date and time


## Application Apearance ##
ctK.set_appearance_mode("Dark")  
ctK.set_default_color_theme("blue")


class App(ctK.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configure Window
        self.title("Network Security Analysis")
        self.geometry(f"{800}x{500}")
    

        # Configure Grid Layout for Application
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Label for Application
        self.label_frame = ctK.CTkFrame(self, fg_color="transparent")
        self.label_frame.grid(row=0, column=0, sticky="nsew")
        self.label = ctK.CTkLabel(self.label_frame, text="Network Security Analysis", font=ctK.CTkFont(size=35, weight="bold"), text_color='light blue')
        self.label.grid(row=0, column=0, padx=20, pady=20)        
        
        # Number of ports and User Input
        self.number_port_frame = ctK.CTkFrame(self, fg_color="transparent")
        self.number_port_frame.grid(row=1, column=0, sticky="nsew")
        self.number_port = ctK.CTkLabel(self.number_port_frame, text="Enter the number of ports that need to be scanned: (Max: 65535)  ", font=ctK.CTkFont(size=20), text_color='white')
        self.number_port.grid(row=1, column=0, padx=20, sticky="sw")
        self.num_entry = ctK.CTkEntry(self.number_port_frame)
        self.num_entry.grid(row=1, column=0, padx=625, sticky="e")

        # User Enters IP ADDRESS or WEB ADDRESS
        self.ip_address_frame = ctK.CTkFrame(self, fg_color="transparent")
        self.ip_address_frame.grid(row=2, column=0, sticky="nsew")
        self.ip_address = ctK.CTkLabel(self.ip_address_frame, text="Enter The Targets (Use Comma to seperate multiple targets): ", font=ctK.CTkFont(size=20), text_color='white')
        self.ip_address.grid(row=2, column=0,  padx=20, sticky="w")
        self.ip_entry = ctK.CTkEntry(self.ip_address_frame, width=175)
        self.ip_entry.grid(row=2, column=0, padx=600, sticky="e")
        
        
        # Create Scan Button
        self.scan_button_frame = ctK.CTkFrame(self, fg_color="transparent")
        self.scan_button_frame.grid(row=3, column=0, sticky="nsew")
        self.scan_button = ctK.CTkButton(self.scan_button_frame, text= 'SCAN',command=self.scan_button)
        self.scan_button.grid(row=3, column=0, padx=20, sticky="s")
            
    def scan_button(self):
        def scan(sip, num):                                                             # Defining function Scan with the parameters sip and num, sip is short for Selected IP Address, num is short for Number of ports
            try:                                                                        # Try- Except Statement statement allows the program to take alternative actions in case of an error.                               
                checked_ip = check_ip(sip)                                              # Creates a variable that checks the Selected IP 
                for port in range(1, num):                                              # Creates a range of ports to scan, 1 being the minimum number of ports and max being the user's input.
                    threading.Thread(target=port_scan, args=(sip, port)).start()        # Thread is a class in the module, 'target =' means the threads all execute the Port Scan Function, 'args' allows us to pass variables to a function.          
                print('\n\nScan Complete')                                              # Prints out a message if previous argument is completed.
            except:
                print('Invalid Address: ' + sip)                                        # Except function used to provide a message to user if Address is invalid.


        ## Returns the Banner if Available ##
                
        def get_banner(s):          # Defining function Get Banner and assiging variable/parameter s to it.                    
            return s.recv(1024)     # The Return Statement is used to send back the results (Name of port) to the user. recv.(1024) is the maximum amount of bytes to be proccessed. 


        ## Converts the Web Address into IP address and returns it ##

        def check_ip(cip):                           # Defining the function Check IP with the parameter 'CIP' short for Check IP.                    
            try:                                     # Try- Except Statement statement allows the program to take alternative actions in case of an error.
                IP(cip)                              # IP Module checks to see if 'CIP' is a Valid IP Address or a Hostname. 
                return cip                           # The Return Statement sends back the results of 'CIP' to the user.
            except ValueError:                       # Value Error Occurs if 'CIP' isnt in a valid IP Address, intsead it is a Hostname or a Web Address.
                return socket.gethostbyname(cip)     # If 'CIP' is a Hostname. The funtion converts it to a Valid IP Adress and Returns output to the user.

            
        ## Checking if the Port is Open or Not ##
            
        def port_scan(sip, port):                                                                                   # Function Port Scan has two parameters, 'SIP' and 'port'.     
            try:                                                                                                    # Try- Except Statement statement allows the program to take alternative actions in case of an error.
                sock = socket.socket()                                                                              # Allocating Sock to the socket object, which is used for Network Communication.
                sock.settimeout(1)                                                                                  # This creates a 1 second timeout on the socket. Which is plenty time to make a connection with the Port. 
                sock.connect((sip, port))                                                                           # The Connect Method tries to Establish a TCP connection the the allocated 'SIP' and 'Port'.
                try:                                                                                                # Try- Except Statement statement allows the program to take alternative actions in case of an error.
                    banner = get_banner(sock)                                                                       # Assigning Banner variable to Get Banner from Socket
                    print("\n[+] Open Port "+str(port)+" of "+str(sip)+" : "+str(banner.decode().strip('\n')))      # If the port has a assigned Banner, function will print the Port, IP Address and the Banner   
                except:                                                                                             
                    print("\n[+] Open Port "+str(port)+" of "+str(sip))                                             # If there is no Banner for the port, the except function will only print the Port and IP Address
            except(socket.timeout, ConnectionRefusedError):                                                         # 'socket.timeout()' occurs when a socket operation exceeds the timeout. Connection Refused error occurs when there is a firewall or refused socket entry.
                pass                                                                                                # The Pass statemnet signals the try-loop there is no code to execute.
            finally:                                                                                                # The Finally Statement means, this section of code will always be executed. 
                sock.close()

        num = int(self.num_entry.get())
        ip_add = str(self.ip_entry.get())
        print("\nScanning started at: " + str(datetime.now()))                               
        start = time.time()                                                                 
        print('\nSearching for Open Ports, Please wait.')                                    
        if ',' in ip_add:                                                                   
            for ip in ip_add.split(','):                                                      
                scan(ip.strip(' '), num)                                                    
        else:                                                                                
            scan(ip_add, num)
        end = time.time()
        elasped = end - start                                                               
        print('\nTime Elasped,', round(elasped,2), 'seconds.')
        
        
                                

if __name__ == "__main__":
    app = App()
    app.mainloop()
 
