**Network Security Analysis - GUI Port Scanner**

This is beginner-friendly **port scanner with a GUI** built using Python's `customtkinter`, `socket`, and `threading` libraries. This tool allows users to scan multiple IP addresses or hostnames for open ports and retrieve service banners if available.

**Features:**

- User-friendly graphical interface (Dark theme)
- Supports IP addresses and hostnames
- Scan multiple targets (comma-separated)
- Specify number of ports (up to 65535)
- Multithreaded scanning for speed and responsiveness
- Banner grabbing (displays service details on open ports)

**Requirements:**

It is required to install the Customtkinter Library for the GUI to Work. 
It can be done on Windows by using the command `pip install customtkinter IPy`.

**How It Works:**

- Uses `socket` to attempt TCP connections to each port.
- If connected, tries to receive a banner (service identification).
- IP and hostname validation handled by `IPy` and `socket.gethostbyname()`.
- Results print to console

**Screenshot Example:**


