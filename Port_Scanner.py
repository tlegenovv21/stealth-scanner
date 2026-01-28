import socket
import threading
import sys
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    sys.exit()

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) 
        
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                # Attempt to grab the service banner
                # We try to receive 1024 bytes of data
                banner = s.recv(1024).decode().strip()
                print(f"[+] Port {port} is OPEN | Banner: {banner}")
            except:
                # Some ports (like Windows 445) won't send data first, they wait for you.
                print(f"[+] Port {port} is OPEN | (No banner received)")
        s.close()
    except Exception:
        pass

# Using threading to scan multiple ports simultaneously
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()