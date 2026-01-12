import socket

def scan_port(ip, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout so it doesn't wait forever on closed ports
    s.settimeout(0.5)

    # connect_ex returns 0 if the connection is successful (port open)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

target = input('ENTER TARGET IP: ') # Localhost or target IP
for port in range(1, 1025):  # Scan common ports 1-1024
    scan_port(target, port)
input('Press ENTER to exit:  ')