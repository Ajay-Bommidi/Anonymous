Anonymous
Anonymous is a Python-powered cybersecurity tool inspired by cyber-thriller movies, designed to cloak your digital identity for educational purposes. As one of my first projects, it transforms you into a digital ghost, masking your online presence through IP anonymization and secure browsing. Evolved concepts from this project live on in my later work, like PassFort and ScanHammer.
🚀 Why Anonymous?
In a world where every click leaves a trace, Anonymous empowers you to:

Hide Your Digital Footprint: Mask your IP and anonymize online activity to explore the web incognito.
Learn Cybersecurity: Master tools like Tor and proxies through hands-on experimentation.
Showcase Skills: A portfolio gem highlighting Python, networking, and ethical hacking for recruiters.
Channel Movie Magic: Live the Mr. Robot fantasy, ethically and safely.


Disclaimer: For EDUCATIONAL USE ONLY. Unauthorized use to harm systems or networks is ILLEGAL and UNETHICAL. Always obtain permission for testing.

📸 Showcase: Become a Digital Ghost
Prove Anonymous works! Share screenshots or GIFs of:

CLI masking your IP or routing through Tor.
Anonymous browsing or Git commit results.
Comparison with tools like Tor Browser.

Example Screenshot:



🛠️ Features

IP Anonymization: Routes traffic through proxies or Tor for untraceable browsing.
Anonymous Commits: Submits Git commits without revealing your identity (inspired by GitMask).
CLI Interface: Simple, Python-driven commands for seamless control.
Educational Focus: Learn anonymity techniques in a safe, controlled environment.

📋 Prerequisites

Operating System: Kali Linux, Ubuntu, or any Linux distro (Windows/macOS may require tweaks).
Python: Version 3.8 or higher.
System Tools: tor, curl (optional for proxy testing).
Dependencies: Python libraries (requests, stem for Tor control).

🛠️ Installation

Clone the Repository:
```
git clone https://github.com/Ajay-Bommidi/Anonymous.git
cd Anonymous
```

Install System Dependencies:
```
sudo apt update
sudo apt install tor curl
```


Set Up Python Environment:
```
python3 -m venv venv
source venv/bin/activate
```


Install Python Dependencies:
```
pip install -r requirements.txt
```

Example requirements.txt:
requests==2.28.1
stem==1.8.0


🚀 Usage
Run the Anonymous CLI:
```
python3 Anonymous.py
```

Menu Options

Mask IP:

Routes traffic through Tor or a proxy.
Example:python3 anonymous.py --mask-ip --tor

Output: New IP address (e.g., via Tor exit node).

Exit:

Closes the CLI.

🧪 Testing Environment

Local Setup: Use a VM (e.g., Kali Linux in VirtualBox) to test anonymity safely.
Verify Anonymity:curl --proxy socks5h://127.0.0.1:9050 http://checkip.amazonaws.com


Capture Screenshots: Show CLI output or browser IP checks and share via GitHub issues.

🔒 Ethical Considerations
Anonymous is for educational testing only. Key safeguards:

Disclaimers: Warns against illegal use.
Controlled Scope: Limits functionality to prevent harm.
Legal Warning: Unauthorized anonymity to bypass laws is illegal (e.g., CFAA in the US).

🤝 Contributing
Help make Anonymous legendary! To contribute:

Fork the repository.
Create a branch: git checkout -b feature-name.
Commit changes: git commit -m "Add feature".
Push: git push origin feature-name.
Open a pull request.

Ideas:

Add proxy rotation for enhanced anonymity.
Share screenshots of anonymized browsing.
Suggest GUI integration (like Strongify).

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
📬 Contact

Author: Ajay Bommidi

GitHub: Ajay-Bommidi

Email: ajaynaidu641@gmail.com

Linkedin : https://www.linkedin.com/in/ajay-bommidi-88b74b279


⭐ Star this repository to support my early cybersecurity adventures! Explore my evolved projects like PassFort and ScanHammer for more advanced tools.
