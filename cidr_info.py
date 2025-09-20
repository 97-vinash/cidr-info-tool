import re
import sys
import argparse

def check_input(input_ip_divided):
    input_ip_decimal = []
    for num in input_ip_divided:
        if num.isdigit():
            input_ip_decimal.append(int(num))
        else:
            raise ValueError("Invalid IP! (use numbers).")
    
    for num in input_ip_decimal[:4]:
        if num < 0 or num > 255:
            raise ValueError("Invalid IP Range! try(0-255).")
    
    if input_ip_decimal[4] < 0 or input_ip_decimal[4] > 32:
        raise ValueError("Invalid Network Prefix Range! try (/0 - /32).")
    
    if len(input_ip_divided) != 5:
        raise ValueError("Invalid input! Format must be: x.x.x.x/x")
    
    return input_ip_decimal

def generate_binary_and_decimal_subnet(network_prefix):
    binary_subnet = []
    subnet_decimal = []
    wildcard_bits = []
    
    count = 0
    for _ in range(4):
        octate = ""
        octate2 = ""
        for _ in range(8):
            if count < network_prefix:
                octate += "1"
                octate2 += "0"
            else:
                octate += "0"
                octate2 += "1"
            count += 1
        wildcard_bits.append(octate2)
        binary_subnet.append(octate)
        subnet_decimal.append(int(octate, 2))
    
    return binary_subnet, subnet_decimal, wildcard_bits

def convert_to_binary(input_ip_decimal):
    ip_binary = []
    for each_bin in input_ip_decimal[:4]:
        bit8_bin = bin(each_bin)[2:].zfill(8)
        ip_binary.append(bit8_bin)
    return ip_binary

def get_network_address(ip_binary, network_prefix):
    binary_network_address = []
    decimal_network_address = []
    
    count = 0
    for i in range(4):
        octate = ip_binary[i]
        octate2 = ""
        for bit in octate:
            if count < network_prefix:
                octate2 += bit
            else:
                octate2 += "0"
            count += 1
        binary_network_address.append(octate2)
        decimal_network_address.append(int(octate2, 2))
    
    return binary_network_address, decimal_network_address

def get_broadcast_address(ip_binary, network_prefix):
    binary_broadcast_address = []
    decimal_broadcast_address = []
    
    count = 0
    for i in range(4):
        octate = ip_binary[i]
        octate2 = ""
        for bit in octate:
            if count < network_prefix:
                octate2 += bit
            else:
                octate2 += "1"
            count += 1
        binary_broadcast_address.append(octate2)
        decimal_broadcast_address.append(int(octate2, 2))
    
    return binary_broadcast_address, decimal_broadcast_address

def print_border():
    print("|--------------------------------|---------------------------------------|")

def main():
    parser = argparse.ArgumentParser(description='CIDR IP Notation Information Tool')
    parser.add_argument('ip', help='IP address in CIDR notation (e.g., 192.168.10.2/24)')
    args = parser.parse_args()
    
    input_ip_string = args.ip
    
    try:
        input_ip_divided = re.split(r'[./]', input_ip_string)
        input_ip_decimal = check_input(input_ip_divided)
        
        ip_binary = convert_to_binary(input_ip_decimal)
        binary_subnet, subnet_decimal, wildcard_bits = generate_binary_and_decimal_subnet(input_ip_decimal[4])
        binary_network_address, decimal_network_address = get_network_address(ip_binary, input_ip_decimal[4])
        binary_broadcast_address, decimal_broadcast_address = get_broadcast_address(ip_binary, input_ip_decimal[4])
        
        wildcard_bits_joined = "".join(wildcard_bits)
        ones_count = wildcard_bits_joined.count("1")
        total_ip = pow(2, ones_count)
        
        print("\nCIDR IP Notation Information")
        print("Input:", input_ip_string)
        print()
        
        print_border()
        print("|  Subnet (Decimal)              |  ", end="")
        print(f"{'.'.join(map(str, subnet_decimal)):<37}|")
        print("|  Subnet (Binary)               |  ", end="")
        print(f"{'.'.join(map(str, binary_subnet)):<37}|")
        print_border()
        
        print("|  Network Address (Decimal)     |  ", end="")
        print(f"{'.'.join(map(str, decimal_network_address)):<37}|")
        print("|  Network Address (Binary)      |  ", end="")
        print(f"{'.'.join(map(str, binary_network_address)):<37}|")
        print_border()
        
        print("|  Broadcast Address (Decimal)   |  ", end="")
        print(f"{'.'.join(map(str, decimal_broadcast_address)):<37}|")
        print("|  Broadcast Address (Binary)    |  ", end="")
        print(f"{'.'.join(map(str, binary_broadcast_address)):<37}|")
        print_border()
        
        print("|  Total Number of IPs           | ", f"{total_ip:<37}|")
        print("|  Total IP Range                |  ", end="")
        full_str = ".".join(map(str, decimal_network_address)) + " -> " + ".".join(map(str, decimal_broadcast_address))
        print(f"{full_str:<37}|")
        print_border()
        
        if input_ip_decimal[4] >= 31:
            print("|  Total Usable Host IPs         | ", f"{"0":<37}|")
            print("|  Total Usable Host IP Range    |  "f"{"N/A":<37}|")
        else:
            print("|  Total Usable Host IPs         | ", f"{(total_ip-2):<37}|")
            print("|  Total Usable Host IP Range    |  ", end="")
            decimal_network_address[3] += 1
            decimal_broadcast_address[3] -= 1
            full_str2 = ".".join(map(str, decimal_network_address)) + " -> " + ".".join(map(str, decimal_broadcast_address))
            print(f"{full_str2:<37}|")
        
        print_border()
        print()
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()