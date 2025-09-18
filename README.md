# CIDR Information Tool

It's a command-line tool to get detailed information about IP addresses in CIDR notation.

## Background

- This is my first ever CLI tool, so i was Learning about Networking and Subnetting Concepts in College, so i thought why not create a CIDR info generator since we had to do it manually to solve it everytime and didn't even know if it was correct or not so i gave it a try.  
- I wrote everything in python, even though i don't use python, generally i use C and C++.  
- The Python code i didn't do any improvement, i just wanted it to work. so i just wrote python code for it, it took some hours.  
- The Problem was i didn't knew how to write a command line tool so i had to use AI for it but, i'll learn it later.

## Features

- Subnet mask calculation (decimal and binary)
- Network address calculation (decimal and binary)
- Broadcast address calculation (decimal and binary)
- Total IP count
- Usable host IP range
- Cross-platform compatibility (Windows, Linux, macOS)
- Clean, formatted output

## Installation

### Prerequisites

- Python 3.6 or higher

### Installation Methods

1. **From source**:
   ```bash
   Clone the repository
   git clone https://github.com/97-vinash/cidr-info-tool.git
   cd cidr-info-tool
   
   Install the package
   pip install .
   ```

2. **Using pip directly from GitHub**:
    ```bash
    pip install git+https://github.com/97-vinash/cidr-info-tool.git
    ```
## Usage

1. **Basic Command**:
    ```bash
    cidr-info <IP_ADDRESS/CIDR>
    ```

## Example Output:
    ```bash
    $ cidr-info 192.168.1.1/24
    CIDR IP Notation Information
    Input: 192.168.1.1/24
    |--------------------------------|-----------------------------------------|
    |  Subnet (Decimal)              |    255.255.255.0
    |  Subnet (Binary)               |    11111111.11111111.11111111.00000000
    |--------------------------------|-----------------------------------------|
    |  Network Address (Decimal)     |    192.168.1.0
    |  Network Address (Binary)      |    11000000.10101000.00000001.00000000
    |--------------------------------|-----------------------------------------|
    |  Broadcast Address (Decimal)   |    192.168.1.255
    |  Broadcast Address (Binary)    |    11000000.10101000.00000001.11111111
    |--------------------------------|-----------------------------------------|
    |  Total Number of IPs           |   256
    |  Total IP Range                |    192.168.1.0 -> 192.168.1.255
    |--------------------------------|-----------------------------------------|
    |  Total Usable Host IPs         |   254
    |  Total Usable Host IP Range    |    192.168.1.1 -> 192.168.1.254
    |--------------------------------|-----------------------------------------|
    ```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Created by Avinash Shankar (97-vinash)


⭐ If you find this tool useful, please consider giving it a star on GitHub!