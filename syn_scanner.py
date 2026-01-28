import sys
from scapy.all import *

# Configuration
common_ports = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

if len(sys.argv) == 2:
    target_ip = sys.argv[1]
else:
    print("Syntax: python syn_scanner.py <ip>")
    sys.exit()

print(f"\n[*] Starting Stealth Scan on {target_ip}...")
print("-" * 40)

for port in common_ports:
    # 1. Create packet for this specific port
    packet = IP(dst=target_ip) / TCP(sport=RandShort(), dport=port, flags="S")
    
    # 2. Send and wait (timeout is short to keep it fast)
    response = sr1(packet, timeout=0.5, verbose=0) 
    
    # 3. Analyze
    service_name = common_ports[port]
    
    if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
        print(f"[+] Port {port:<4} ({service_name}): OPEN")
    else:
        # We comment this out to reduce noise, only showing OPEN ports
        # print(f"[-] Port {port:<4} ({service_name}): CLOSED")
        pass

print("-" * 40)
print("[*] Scan Complete.")