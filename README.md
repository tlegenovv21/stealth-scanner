# ⚡ Python Stealth SYN Scanner (Multi-Threaded)

A high-performance network scanner built with **Python** and **Scapy**. This tool performs "Stealth Scans" (TCP Half-Open) and uses **Multi-Threading** to scan thousands of ports in seconds.

## 🚀 Features
* **Stealth Mode:** Uses raw packet manipulation (SYN -> SYN-ACK -> RST) to avoid completing the TCP handshake.
* **Multi-Threading:** Implements `ThreadPoolExecutor` to scan hundreds of ports simultaneously.
* **CLI Arguments:** Full command-line interface using `argparse` for flexible testing.
* **Custom Packet Crafting:** Bypasses standard socket libraries by manually constructing IP/TCP headers.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/stealth-scanner.git](https://github.com/tlegenovv21/stealth-scanner.git)