import subprocess

a = input('Enter URL or IP Address:  ')
subprocess.call('ping ' + a, shell=True)
input('Press ENTER to exit...')