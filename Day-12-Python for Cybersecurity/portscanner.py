import socket

target = input("Enter target IP: ")
ports_to_scan = [21, 22, 80, 443, 3306]
open_count = 0

for port in ports_to_scan:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
        open_count += 1
    else:
        print(f"Port {port} is closed")
    
    sock.close()

print(f"\nScan complete. {open_count} open port(s) found.")
