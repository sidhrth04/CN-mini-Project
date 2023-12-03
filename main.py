import socket

def scan_port(host, port, timeout):
    # Scan the specified TCP port on the target IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} : open")
        else:
            print(f"Port {port} : closed")
    except socket.gaierror:
        print(f'Error: Could not resolve hostname {host}')
    except socket.error as e:
        print(f'Error: Could not connect to {host}:{port} ({e})')
    finally:
        s.close()

def scan_prominent_ports(target_host, timeout):
    # List of prominent ports to scan
    prominent_ports = [
        21, 22, 23, 25, 53, 80, 110, 143, 443, 587, 993, 995, 3389, 5432, 8080
        # Add more ports as needed
    ]

    for port in prominent_ports:
        scan_port(target_host, port, timeout)

if _name_ == "_main_":
    target_host = input("Enter the target IP address: ")
    timeout = float(input("Enter the socket timeout in seconds: "))

    print(f"Scanning prominent ports on {target_host}...\n")
    scan_prominent_ports(target_host, timeout)
