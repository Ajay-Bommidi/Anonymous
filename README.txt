# Anonymous

Anonymous is a Python-based tool designed to change your IP address at regular intervals using the Tor network. This tool ensures enhanced privacy by continuously updating your IP address, making it harder to trace your online activities.

## Features

- Automatically changes your IP address at user-defined intervals.
- Configurable wait time after each Tor reload to ensure IP change.
- Interactive user prompts to guide through setup and usage.
- Checks and ensures Tor service and SOCKS proxy are correctly configured.
- Handles errors gracefully, providing clear instructions for troubleshooting.

## Requirements

- Python 3
- pip
- Tor

## Installation
Before running the tool, ensure you have the required packages installed. You can install the necessary Python packages using the `requirements.txt` file.

```sh
pip install -r requirements.txt

'''' Usage: 
sudo python3 anonymous.py

EXAMPLE :
[+] Time to change IP in seconds [type=60] >> 120
[+] How many times do you want to change your IP [type=1000] for infinite IP change type [0] >> 500
[+] Time to wait after reloading Tor (seconds) [type=15] >> 20
