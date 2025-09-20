# CIDR Information Tool

It's a command-line tool to get detailed information about IP addresses in CIDR notation.

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

1. Python 3.6 or higher
2. pip (comes with Python)
3. Git 

### Installation Methods(choose any 1)

1. **Using pip directly from GitHub**:
    ```bash
    pip install git+https://github.com/97-vinash/cidr-info-tool.git
    ```

2. **From source**:
    Clone the repository
    ```bash
    git clone https://github.com/97-vinash/cidr-info-tool.git
    cd cidr-info-tool
    ```
    Install the package
    ```bash
    pip install .
    ```

## Usage

1. **Basic Command**:
    ```bash
    cidr-info <IP_ADDRESS/CIDR>
    ```
    Compatible with Windows/Mac/Linux

## Example Output:

    CIDR IP Notation Information
    Input: 192.168.97.21/13

    |--------------------------------|---------------------------------------|
    |  Subnet (Decimal)              |  255.248.0.0                          |
    |  Subnet (Binary)               |  11111111.11111000.00000000.00000000  |
    |--------------------------------|---------------------------------------|
    |  Network Address (Decimal)     |  192.168.0.0                          |
    |  Network Address (Binary)      |  11000000.10101000.00000000.00000000  |
    |--------------------------------|---------------------------------------|
    |  Broadcast Address (Decimal)   |  192.175.255.255                      |
    |  Broadcast Address (Binary)    |  11000000.10101111.11111111.11111111  |
    |--------------------------------|---------------------------------------|
    |  Total Number of IPs           |  524288                               |
    |  Total IP Range                |  192.168.0.0 -> 192.175.255.255       |
    |--------------------------------|---------------------------------------|
    |  Total Usable Host IPs         |  524286                               |
    |  Total Usable Host IP Range    |  192.168.0.1 -> 192.175.255.254       |
    |--------------------------------|---------------------------------------|

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Created by [97-vinash](https://www.linkedin.com/in/avinash-shankar-643809249/)

## Backstory

- This is my first ever CLI tool, so i was Learning about Networking and Subnetting Concepts in College, so i thought why not create a CIDR info generator since we had to do it manually to solve it everytime and didn't even know if it was correct or not so i gave it a try.  
- I wrote everything in python, even though i don't use python, generally i use C and C++.  
- The Python code i didn't do any improvement, i just wanted it to work. so i just wrote python code for it, it took some hours.  
- The Problem was i didn't knew how to write a command line tool so i had to use AI for it but, i'll learn it later.

---
⭐ If you find this tool useful, please consider giving it a star on [GitHub](https://github.com/97-vinash/cidr-info-tool)