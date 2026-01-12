import subprocess

ip = input("Enter the IP address or URL: ")
subprocess.call(["tracert", ip])
input("Press any enter to exit...")
