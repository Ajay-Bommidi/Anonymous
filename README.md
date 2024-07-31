# Anonymous
Tool that makes u Anonumous on the Internet it eill chnage our IPAddress for every 5 seconds and makes u anonymous on internet
# Anonymous

Anonymous is a powerful Python-based tool designed to change your IP address at regular intervals using the Tor network. This tool provides enhanced privacy and security by continuously updating your IP address, making it significantly harder for anyone to trace your online activities.

## Features

- **Automatic IP Change**: Automatically changes your IP address at user-defined intervals, ensuring continuous anonymity.
- **Configurable Wait Time**: Allows users to set a wait time after each Tor reload to ensure the new IP address is properly applied.
- **Interactive Prompts**: Guides users through setup and usage with interactive prompts.
- **Error Handling**: Gracefully handles errors and provides clear instructions for troubleshooting.
- **Proxy Check**: Ensures that the SOCKS proxy is correctly configured to `127.0.0.1:9050`.

## Power of Anonymous

Anonymous leverages the Tor network to provide a robust mechanism for maintaining online anonymity. By regularly changing your IP address, it makes tracking your online presence much more difficult. This tool is ideal for users who require a higher level of privacy, such as journalists, activists, and anyone concerned about online surveillance.

## Requirements

- Python 3
- pip
- Tor

## Installation
 **Install Python Packages**:
 ```sh
 sudo git clone https://github.com/Hunter8309799/Anonymous.git
   cd Anonymous
   pip install -r requirements.txt
   sudo apt update
   sudo apt install tor -y
# Run the script :
  sudo python3 anonyms.py
