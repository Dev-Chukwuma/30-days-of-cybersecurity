import socket


def scan_port(target, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0


def scan_target(target, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)
    
    return open_ports


def save_results(target, open_ports):
    filename = f"scan_{target}.txt"
    
    with open(filename, "w") as f:
        f.write(f"Scan results for {target}\n")
        f.write(f"Open ports: {open_ports}\n")
    
    print(f"Results saved to {filename}")


def main():
    target = input("Enter target IP: ")
    
    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        exit()
    
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    
    open_ports = scan_target(target, start_port, end_port)
    
    print(f"\nScan complete. {len(open_ports)} open port(s) found.")
    save_results(target, open_ports)


if __name__ == "__main__":
    main()
