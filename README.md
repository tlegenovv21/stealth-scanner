# 🕵️ Python Stealth SYN Scanner

A lightweight network scanner built with **Python** and **Scapy**. This tool performs a "Stealth Scan" (TCP Half-Open Scan) to identify open ports without completing the 3-way handshake, making it less likely to be logged by target firewalls.

## 🚀 Features
* **Stealth Mode:** Uses raw packet manipulation to send `SYN` packets and analyze `SYN-ACK` vs `RST` responses.
* **Custom Packet Crafting:** Bypasses standard socket libraries by constructing IP/TCP headers manually.
* **Service Detection:** Scans common ports (FTP, SSH, DNS, HTTP, HTTPS) to identify running services.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/stealth-scanner.git](https://github.com/YOUR_USERNAME/stealth-scanner.git)