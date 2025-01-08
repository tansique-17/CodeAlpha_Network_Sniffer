import socket
import struct
import os
import pyfiglet

def main():
    myip = input("Enter your local IP address: ")
    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sniffer.bind((myip, 0)) 
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        # Enable promiscuous mode on Windows
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    except PermissionError:
        print("Permission denied. Run the script as administrator.")
        return

    print("Sniffer is running... Press Ctrl+C to stop.")

    try:
        while True:
            raw_data, addr = sniffer.recvfrom(65565)
            ip_header = raw_data[:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
            ttl = iph[5]
            proto = iph[6]
            src = socket.inet_ntoa(iph[8])
            dest = socket.inet_ntoa(iph[9])
            print(f"Packet: Version={version}, Header Length={ihl * 4}, TTL={ttl}, Protocol={proto}, Source={src}, Destination={dest}")
    except KeyboardInterrupt:
        print("Sniffer stopped.")
    finally:
        # Disable promiscuous mode on Windows
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    print(pyfiglet.figlet_format("Network   Sniffer"))
    main()



