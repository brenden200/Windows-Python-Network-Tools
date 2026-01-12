import subprocess

a = input('Enter URL:  ')
subprocess.call('nslookup' ' ' + a, shell=True)
input('PRESS ENTER TO EXIT... ')

