import subprocess
import netifaces as ni
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
# VERY UNSAFE WAY TO RUN NOTEBOOKS IF THEY HAVE SENSITIVE INFO OR ARE PUBLICALLY ACCESSIBLE!!!
subprocess.Popen("jupyter lab --ip="+ip+" --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''", shell=True)
input()
