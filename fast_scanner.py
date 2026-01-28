import sys
import argparse
from scapy.all import *
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# A lock to stop threads from printing over each other
print_lock = threading.Lock()

def scan_port(ip, port):
    # 1. Create the Stealth Packet (SYN)
    # We use a random source port to look less suspicious
    src_port = RandShort()
    packet = IP(dst=ip)/TCP(sport=src_port, dport=port, flags="S")
    
    # 2. Send and wait (timeout is short because we have many threads)
    resp = sr1(packet, timeout=1, verbose=0)
    
    # 3. Analyze Response
    if resp:
        if resp.haslayer(TCP):
            # 0x12 = SYN-ACK (Open)
            if resp[TCP].flags == 0x12:
                # Send RST to close connection (Stealth)
                send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0)
                
                # Print result safely
                with print_lock:
                    print(f"[+] Port {port:<5} is OPEN")
            
            # 0x14 = RST-ACK (Closed)
            elif resp[TCP].flags == 0x14:
                pass # Closed port, ignore
                
    else:
        # No response usually means filtered/firewalled
        pass

def main():
    # Professional Argument Parsing
    parser = argparse.ArgumentParser(description="Python Stealth SYN Scanner")
    parser.add_argument("-t", "--target", help="Target IP Address", required=True)
    parser.add_argument("-s", "--start", help="Start Port", type=int, default=1)
    parser.add_argument("-e", "--end", help="End Port", type=int, default=1024)
    parser.add_argument("-th", "--threads", help="Number of Threads", type=int, default=50)
    
    args = parser.parse_args()
    target_ip = args.target

    # Banner
    print("-" * 50)
    print(f"[*] Scanning Target: {target_ip}")
    print(f"[*] Port Range:      {args.start} - {args.end}")
    print(f"[*] Threads:         {args.threads}")
    print(f"[*] Time Started:    {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    # Multi-Threading Magic
    # We create a 'pool' of workers (threads) and give them tasks
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        # Create a list of ports to scan
        ports = range(args.start, args.end + 1)
        
        # Launch the scan!
        for port in ports:
            executor.submit(scan_port, target_ip, port)

    print("-" * 50)
    print("[*] Scan Complete.")

if __name__ == "__main__":
    main()