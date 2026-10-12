Network Packet Analyzer

About the Project

The Network Packet Analyzer is a Python-based cybersecurity project that analyzes network packets from a saved packet capture file (".cap" or ".pcap").

It uses the Scapy library to examine packet information and display source IP addresses, destination IP addresses, IP versions, transport protocols, and protocol statistics.

This project was developed as a beginner-friendly introduction to network traffic analysis and defensive cybersecurity.

Features

- Reads saved network packet capture files.
- Supports IPv4 and IPv6 packets.
- Identifies TCP and UDP transport protocols.
- Displays source and destination IP addresses.
- Counts packets by transport protocol.
- Displays packet analysis results in the terminal.
- Handles missing files and packet-reading errors.

Technologies Used

- Python
- Scapy
- Visual Studio Code

Project Structure

CodeAlpha_BasicNetworkSniffer/
├── sniffer.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/

The ".venv/" directory contains the local Python virtual environment and should not be uploaded to GitHub.

Requirements

- Python 3
- Scapy
- A saved network packet capture file

Installation and Usage

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

Replace "YOUR_GITHUB_REPOSITORY_URL" with your repository URL.

2. Open the project directory

cd CodeAlpha_BasicNetworkSniffer

3. Install the dependency

pip install -r requirements.txt

4. Run the analyzer

python sniffer.py

5. Enter the capture file path

When prompted, enter the path to a packet capture file on your computer.

For example:

v6-http.cap

The capture file must exist at the path you enter.

Sample Output

The program displays information such as:

- Total packets analyzed
- Packet number
- IP version
- Source IP address
- Destination IP address
- Transport protocol
- Protocol statistics

Cybersecurity Learning Outcomes

This project provides practical experience with:

- Network packet analysis
- IPv4 and IPv6 addressing
- TCP and UDP protocols
- Python scripting
- Scapy fundamentals
- Basic defensive security analysis

Limitations

This version analyzes previously saved packet capture files. It does not capture live network traffic.

The accuracy and completeness of the analysis depend on the contents of the capture file.

Disclaimer

This project is intended for educational and authorized defensive cybersecurity learning. Analyze only packet captures you are permitted to access.

Author

Kavi

Cybersecurity Learner | BSc Computer Science