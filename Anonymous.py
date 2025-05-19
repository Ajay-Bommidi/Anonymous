# -*- coding: utf-8 -*-
import os
import subprocess
import requests
from requests.exceptions import RequestException
import asyncio

# Colored output
def cprint(msg, color="green", prefix="[+]"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, '')}{prefix} {msg}{colors['reset']}")

def banner():
    os.system("clear")
    print("""
\033[95m
 
    ___                                                      
   /   |  ____  ____  ____  __  ______ ___  ____  __  _______
  / /| | / __ \/ __ \/ __ \/ / / / __ `__ \/ __ \/ / / / ___/
 / ___ |/ / / / /_/ / / / / /_/ / / / / / / /_/ / /_/ (__  ) 
/_/  |_/_/ /_/\____/_/ /_/\__, /_/ /_/ /_/\____/\__,_/____/  
                         /____/                              
                       
 
 
 \033[0m
                              \033[96m~ Anonymous.. | Be Anonymous Online ~\033[0m
""")

def check_sudo():
    if os.geteuid() != 0:
        cprint("This script requires root permissions. Please run with 'sudo'.", "red", "[!]")
        exit(1)

def install_package(package_name):
    try:
        subprocess.check_output(f'dpkg -s {package_name}', shell=True, stderr=subprocess.DEVNULL)
        cprint(f"{package_name} is already installed.")
    except subprocess.CalledProcessError:
        cprint(f"{package_name} is not installed. Installing...", "yellow")
        try:
            subprocess.check_output('sudo apt update', shell=True, stderr=subprocess.DEVNULL)
            subprocess.check_output(f'sudo apt install {package_name} -y', shell=True, stderr=subprocess.DEVNULL)
            cprint(f"{package_name} installed successfully.", "green", "[✔]")
        except subprocess.CalledProcessError as e:
            cprint(f"Failed to install {package_name}: {e}", "red", "[!]")
            exit(1)

def install_python_package(package_name):
    try:
        subprocess.check_output(f'pip3 show {package_name}', shell=True, stderr=subprocess.DEVNULL)
        cprint(f"{package_name} is already installed.")
    except subprocess.CalledProcessError:
        cprint(f"{package_name} is not installed. Installing...", "yellow")
        os.system(f'pip3 install {package_name} > /dev/null 2>&1')
        cprint(f"{package_name} installed successfully.", "green", "[✔]")

def setup_environment():
    install_package('python3-pip')
    install_python_package('requests[socks]')
    install_package('tor')

def check_proxy():
    try:
        cprint("Checking SOCKS proxy on 127.0.0.1:9050...", "cyan")
        response = requests.get('https://api64.ipify.org?format=json', proxies={
            "http": "socks5h://127.0.0.1:9050",
            "https": "socks5h://127.0.0.1:9050"
        }, timeout=5)
        if response.status_code == 200:
            cprint("SOCKS proxy is working and correctly configured.")
        else:
            cprint("SOCKS proxy check failed.", "red", "[!]")
            exit(1)
    except RequestException:
        cprint("Unable to connect using SOCKS proxy. Check Tor status and proxy settings.", "red", "[!]")
        exit(1)

def get_current_ip():
    url = 'https://api64.ipify.org?format=json'
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        return response.json().get('ip', 'Error')
    except RequestException as e:
        cprint(f"Error retrieving IP: {e}", "red", "[!]")
        return "Error"

async def change_ip():
    cprint("Reloading Tor service for new identity...", "yellow")
    os.system("service tor reload")
    await asyncio.sleep(10)
    new_ip = get_current_ip()
    cprint(f"Your new IP address: {new_ip}", "green", "[IP]")
    return new_ip

def start_tor_service():
    cprint("Starting Tor service...", "cyan")
    try:
        subprocess.check_output('service tor start', shell=True, stderr=subprocess.DEVNULL)
        cprint("Tor service started successfully.", "green", "[✔]")
    except subprocess.CalledProcessError as e:
        cprint(f"Failed to start Tor service: {e.output.decode().strip()}", "red", "[!]")
        exit(1)

async def run_tool(interval, times):
    if times == 0:
        count = 1
        while True:
            try:
                cprint(f"[∞-{count}] Changing IP...", "cyan")
                await asyncio.sleep(interval)
                await change_ip()
                count += 1
            except KeyboardInterrupt:
                cprint("Anonymous.. is closing.", "yellow", "\n[EXIT]")
                break
    else:
        for i in range(times):
            cprint(f"[{i+1}/{times}] Changing IP...", "cyan")
            await asyncio.sleep(interval)
            await change_ip()

def main():
    check_sudo()
    setup_environment()
    banner()
    cprint("Tip: Set your browser or system proxy to 127.0.0.1:9050", "yellow", "[INFO]")
    start_tor_service()
    check_proxy()

    try:
        interval = int(input("\n[?] Interval in seconds between IP changes (default: 60): ") or 60)
        times = int(input("[?] Number of IP changes (default: 1000, use 0 for infinite): ") or 1000)
        cprint(f"Starting Anonymous.. with interval = {interval}s and count = {times}", "green", "[RUN]")
        asyncio.run(run_tool(interval, times))
    except ValueError:
        cprint("Invalid input. Please enter numeric values.", "red", "[!]")
        exit(1)

if __name__ == "__main__":
    main()
