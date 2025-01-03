# CodeAlpha_Network_Sniffer


```markdown
# Network Packet Sniffer

This is a simple network packet sniffer built using Python's `socket` and `struct` modules. It captures and analyzes raw network packets, displaying key information about each packet, including the version, header length, TTL (Time to Live), protocol, and source/destination IP addresses.

## Features

- Captures all network packets on the local network.
- Displays important details of the captured packets:
  - IP Version
  - Header Length
  - TTL (Time to Live)
  - Protocol
  - Source and Destination IP addresses
- Supports both Linux/macOS and Windows (with a slight modification for promiscuous mode on Windows).

## Requirements

- Python 3.x
- Root/Administrator privileges (for capturing raw packets)

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/tansique-17/CodeAlpha_network_sniffer.git
   cd CodeAlpha_network_sniffer
   ```

2. Install the necessary dependencies:

   This script uses the built-in `socket` and `struct` libraries, so no external dependencies are required.

3. Run the script with elevated privileges:

   On Linux/macOS:
   ```bash
   sudo python3 sniffer.py
   ```

   On Windows:
   Run the script as Administrator (right-click and "Run as Administrator").

## Usage

- The sniffer starts capturing packets immediately upon running the script.
- The packet details will be printed to the console.
- You can stop the sniffer anytime by pressing `Ctrl+C`.

Example output:
```
Packet: Version=4, Header Length=20, TTL=128, Protocol=6, Source=192.168.0.1, Destination=192.168.0.102
Packet: Version=4, Header Length=20, TTL=64, Protocol=17, Source=10.0.0.5, Destination=192.168.0.102
```

## Notes

- On Windows, the script enables promiscuous mode to capture all packets. Be sure to run the script with administrator privileges to allow this feature.
- The script captures only the first 20 bytes of the IP header to gather basic packet information.
- This script is intended for educational and debugging purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This packet sniffer should only be used on networks you have permission to monitor. Unauthorized packet sniffing is illegal in many jurisdictions.
```
