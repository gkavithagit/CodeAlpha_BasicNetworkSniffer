from scapy.all import rdpcap, IP, IPv6, TCP, UDP
from collections import Counter
from pathlib import Path


def analyze_packets(file_path):
    path = Path(file_path)

    if not path.is_file():
        print("Error: Packet file not found.")
        return

    try:
        packets = rdpcap(str(path))
    except Exception as error:
        print(f"Error reading packet file: {error}")
        return

    protocol_counts = Counter()

    print("\n" + "=" * 45)
    print("       NETWORK PACKET ANALYZER")
    print("=" * 45)
    print(f"\nTotal Packets Analyzed: {len(packets)}")

    for packet_number, packet in enumerate(packets, start=1):

        if IP in packet:
            source_ip = packet[IP].src
            destination_ip = packet[IP].dst
            ip_version = "IPv4"

        elif IPv6 in packet:
            source_ip = packet[IPv6].src
            destination_ip = packet[IPv6].dst
            ip_version = "IPv6"

        else:
            protocol_counts["Non-IP"] += 1
            continue

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "Other"

        protocol_counts[protocol] += 1

        print("\n" + "-" * 45)
        print(f"Packet Number: {packet_number}")
        print(f"IP Version: {ip_version}")
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Transport Protocol: {protocol}")

    print("\n" + "=" * 45)
    print("       PROTOCOL STATISTICS")
    print("=" * 45)

    for protocol, count in protocol_counts.items():
        print(f"{protocol}: {count}")

    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    file_name = input(
        "Enter the path to your packet capture file: "
    ).strip().strip('"')

    analyze_packets(file_name)