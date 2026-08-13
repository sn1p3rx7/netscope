#!/usr/bin/env python3
import getpass
import platform
import socket
import subprocess


VERSION = "0.1.0"


def system_info():
    print("\n[ SYSTEM ]")
    print(f"OS:       {platform.system()}")
    print(f"Release:  {platform.release()}")
    print(f"Machine:  {platform.machine()}")
    print(f"Python:   {platform.python_version()}\n")


def network_info():
    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "Unknown"

    print("\n[ NETWORK ]")
    print(f"Hostname: {hostname}")
    print(f"Local IP: {ip}\n")


def ping(host):
    print(f"\n[ PING ] {host}")

    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print("Status: ONLINE\n")
    else:
        print("Status: OFFLINE\n")

def processes():
    print("\n[ PROCESSES ]")

    result = subprocess.run(
        ["ps", "-eo", "pid,comm,%cpu,%mem"],
        capture_output=True,
        text=True
    )

    print(result.stdout)
def ports():
    print("\n[ LISTENING PORTS ]")

    result = subprocess.run(
        ["ss", "-tuln"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Unable to read ports.\n")
        return

    print(result.stdout)
def info():
    print("\n========== NetScope ==========\n")

    system_info()
    network_info()
    processes()
    ports()
def help_menu():
    print("""
Available commands:

  help                 Show this help
  system               Show system information
  network              Show network information
  ping <host>          Ping a host
  version              Show NetScope version
  clear                Clear terminal
  exit                 Exit NetScope
  processes            Show running processes
  ports                Show listening ports
""")


def main():
    username = getpass.getuser()

    print("""
╭──────────────────────────────╮
│          NetScope             │
│     System & Network CLI      │
╰──────────────────────────────╯
Type "Help" To View Commands
""")

    while True:
        try:
            command = input(f"NetScope@{username}> ").strip()

            if not command:
                continue

            parts = command.split()
            cmd = parts[0].lower()

            if cmd == "help":
                help_menu()

            elif cmd == "system":
                system_info()

            elif cmd == "network":
                network_info()
            elif cmd == "processes":
                processes()
            elif cmd == "info":
                info()
            elif cmd == "ping":
                if len(parts) < 2:
                    print("Usage: ping <host>\n")
                else:
                    ping(parts[1])

            elif cmd == "version":
                print(f"NetScope {VERSION}\n")

            elif cmd == "clear":
                subprocess.run(["clear"])

            elif cmd == "exit":
                print("Goodbye!")
                break
            elif cmd == "ports":
                ports()

            else:
                print(f"Unknown command: {cmd}")
                print("Type 'help' for available commands.\n")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.\n")


if __name__ == "__main__":
    main()
