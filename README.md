# NetScope

A lightweight system and network diagnostic CLI for Linux.

## Features

- System information
- Network information
- Process monitoring
- Listening ports
- Host ping
- Interactive CLI

## Installation

Clone the repository
```bash
git clone https://github.com/sn1p3rx7/netscope
```
Enter the project:

    cd netscope

Run the installer:

    ./install/linux.sh

if no work 
```bash
cd netscope && sudo chmod +x./install/linux.sh
sudo bash ./install/linux.sh
```
## Usage

Start NetScope:

    netscope

Available commands:

    help
    system
    network
    processes
    ports
    ping <host>
    version
    clear
    exit

## Project Structure

    netscope/
    ├── src/
    │   └── main.py
    ├── install/
    │   └── linux.sh
    ├── README.md
    ├── LICENSE
    └── .gitignore

## Status

Version: 0.1.0

NetScope is currently in early development.
# No Value Info
NetScope Using `Python` programing Laungage
And Using `bash` to Install

