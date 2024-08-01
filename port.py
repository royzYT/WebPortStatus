import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is {ip_address}")
        return ip_address
    except socket.gaierror:
        print(f"Couldn't resolve the domain {domain}")
        return None

def scan_ports(ip_address, start_port, end_port):
    print(f"Scanning ports on {ip_address}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))

        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        sock.close()

if __name__ == "__main__":
    target_domain = input("Enter the target domain: ")
    target_ip = get_ip_address(target_domain)

    if target_ip:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))

        scan_ports(target_ip, start_port, end_port)