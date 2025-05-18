# -*- coding: utf-8 -*-
import time
import os
import subprocess
import requests
from requests.exceptions import RequestException
import asyncio

def check_sudo():
    """Check if the script is running with sudo permissions."""
    if os.geteuid() != 0:
        print("[!] This script requires root permissions. Please run with 'sudo'.")
        exit(1)

def install_package(package_name):
    """Install a system package if not already installed."""
    try:
        subprocess.check_output(f'dpkg -s {package_name}', shell=True)
        print(f'[+] {package_name} is already installed.')
    except subprocess.CalledProcessError:
        print(f'[+] {package_name} is not installed. Installing...')
        try:
            subprocess.check_output('sudo apt update', shell=True, stderr=subprocess.DEVNULL)
            subprocess.check_output(f'sudo apt install {package_name} -y', shell=True, stderr=subprocess.DEVNULL)
            print(f'[!] {package_name} installed successfully.')
        except subprocess.CalledProcessError as e:
            print(f"[!] Failed to install {package_name}: {e}")
            exit(1)

def install_python_package(package_name):
    """Install a Python package if not already installed."""
    try:
        subprocess.check_output(f'pip3 show {package_name}', shell=True)
        print(f'[+] {package_name} is already installed.')
    except subprocess.CalledProcessError:
        print(f'[+] {package_name} is not installed. Installing...')
        try:
            os.system(f'pip3 install {package_name} > /dev/null 2>&1')
            print(f'[!] {package_name} installed successfully.')
        except subprocess.CalledProcessError as e:
            print(f"[!] Failed to install {package_name}: {e}")
            exit(1)

def setup_environment():
    """Check and install required packages."""
    install_package('python3-pip')
    install_python_package('requests[socks]')
    install_package('tor')

def check_proxy():
    """Check if the SOCKS proxy is set to 127.0.0.1:9050."""
    try:
        response = requests.get('https://api64.ipify.org?format=json', proxies={
            "http": "socks5h://127.0.0.1:9050",
            "https": "socks5h://127.0.0.1:9050"
        }, timeout=5)
        if response.status_code == 200:
            print('[+] SOCKS proxy is correctly configured to 127.0.0.1:9050.')
        else:
            print("[!] SOCKS proxy is not correctly configured. Please ensure it is set to 127.0.0.1:9050.")
            exit(1)
    except RequestException:
        print("[!] Unable to connect using SOCKS proxy. Please check your proxy settings.")
        exit(1)

def ma_ip():
    """Retrieve the current external IP address."""
    url = 'https://api64.ipify.org?format=json'
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    try:
        response = requests.get(url, proxies=proxies)
        return response.json().get('ip', 'Error')
    except RequestException as e:
        print(f"[!] Error retrieving IP: {e}")
        return "Error"

async def change_ip():
    """Reload Tor service and print the new IP address."""
    print("[+] Reloading Tor service...")
    os.system("service tor reload")
    await asyncio.sleep(10)  # Wait to ensure Tor has time to reload and apply changes
    new_ip = ma_ip()
    print(f'[+] Your IP has been changed to: {new_ip}')
    return new_ip

def start_tor_service():
    """Start the Tor service and check its status."""
    print("[+] Starting Tor service...")
    try:
        subprocess.check_output('service tor start', shell=True, stderr=subprocess.STDOUT)
        print('[+] Tor service started successfully.')
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to start Tor service: {e.output.decode().strip()}")
        print("[!] Please ensure that Tor is installed and configured correctly.")
        exit(1)

async def run_tool(interval, times):
    """Run the IP change tool for the specified number of times or indefinitely."""
    if times == 0:
        while True:
            try:
                await asyncio.sleep(interval)
                await change_ip()
            except KeyboardInterrupt:
                print('\nAuto TOR is closed.')
                break
    else:
        for _ in range(times):
            await asyncio.sleep(interval)
            await change_ip()

def main():
    """Main function to set up the environment and start the tool."""
    check_sudo()
    setup_environment()

    os.system("clear")
    print(''' 
  _______     ______  ______ _____     _____ _____  ______ _____ _______ ____  _____  
 / ____\ \   / /  _ \|  ____|  __ \   / ____|  __ \|  ____/ ____|__   __/ __ \|  __ \ 
| |     \ \_/ /| |_) | |__  | |__) | | (___ | |__) | |__ | |       | | | |  | | |__) |
| |      \   / |  _ <|  __| |  _  /   \___ \|  ___/|  __|| |       | | | |  | |  _  / 
| |____   | |  | |_) | |____| | \ \   ____) | |    | |___| |____   | | | |__| | | \ \ 
 \_____|  |_|  |____/|______|_|  \_\ |_____/|_|    |______\_____|  |_|  \____/|_|  \_\ [Ajay]
''')
    print("\n Be Anonymous online\n")
    print("Make sure to configure your SOCKS proxy to 127.0.0.1:9050")
    
    check_proxy()
    start_tor_service()

    try:
        interval = int(input("[+] Time to change IP in seconds [type=60] >> ") or 60)
        times = int(input("[+] How many times do you want to change your IP [type=1000] for infinite IP change type [0] >> ") or 1000)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_tool(interval, times))
    except ValueError:
        print("[!] Please enter valid numbers for time and iterations.")

if __name__ == "__main__":
    main()

