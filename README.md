# CodeAlpha_Network_Sniffer

## Network Packet Sniffer

This Python script is a simple network packet sniffer that uses the `socket`, `struct`, and `pyfiglet` modules to capture and analyze raw network packets. The script displays a banner with the title "Network Sniffer" using `pyfiglet` and then prints details of captured packets such as IP version, header length, TTL (Time to Live), protocol, and source/destination IP addresses.

## Features

- Captures network packets on the local network.
- Displays key information about the captured packets:
  - IP Version
  - Header Length
  - TTL (Time to Live)
  - Protocol
  - Source and Destination IP addresses
- Displays a "Network Sniffer" banner using `pyfiglet`.
- Supports both Linux/macOS and Windows, with Windows-specific handling for promiscuous mode.

## Requirements

- Python 3.x
- `pyfiglet` library (can be installed via pip)
- Root/Administrator privileges (for capturing raw packets)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tansique-17/CodeAlpha_network_sniffer.git
   cd CodeAlpha_network_sniffer
   ```

2. Install required Python packages:

   This script requires the `pyfiglet` library, which can be installed using `pip`:

   ```bash
   pip install pyfiglet
   ```

3. Install dependencies for raw socket usage (if necessary):

   - On Linux/macOS: You may need to run the script as root.
   - On Windows: Ensure you're running the script as Administrator.

## Usage

To run the script, use the following command:

On Linux/macOS:
```bash
sudo python3 sniffer.py
```

On Windows:
Right-click the script and select "Run as Administrator."

### Example Output:
```
 _   _      _                      _        ____        _  __  __
| \ | | ___| |___      _____  _ __| | __   / ___| _ __ (_)/ _|/ _| ___ _ __ 
|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /   \___ \| '_ \| | |_| |_ / _ \ '__|
| |\  |  __/ |_ \ V  V / (_) | |  |   <     ___) | | | | |  _|  _|  __/ |   
|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\   |____/|_| |_|_|_| |_|  \___|_|   

Sniffer is running... Press Ctrl+C to stop.
Packet: Version=4, Header Length=20, TTL=64, Protocol=6, Source=192.168.0.1, Destination=192.168.0.102
Packet: Version=4, Header Length=20, TTL=128, Protocol=17, Source=10.0.0.5, Destination=192.168.0.102
```

### Captured Packet Information:
- **Version**: IP version (IPv4 or IPv6).
- **Header Length**: Length of the IP header.
- **TTL**: Time-to-Live value, which is used to limit the packet’s lifetime.
- **Protocol**: The transport protocol used (TCP, UDP, etc.).
- **Source**: The source IP address.
- **Destination**: The destination IP address.

## Notes

- On Windows, the script enables promiscuous mode to capture all packets. You must run the script with Administrator privileges to allow this feature.
- This script captures only the first 20 bytes of the IP header to gather basic packet information.
- This packet sniffer is for educational and debugging purposes only.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/tansique-17/CodeAlpha_network_sniffer/LICENSE) file for details.

## Disclaimer

Please ensure you have permission to capture and analyze network traffic before running this script. Unauthorized sniffing of network traffic may be illegal in certain jurisdictions.
