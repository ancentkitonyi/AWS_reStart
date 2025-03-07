import os
import subprocess

# List files in the directory
os.system("dir")
subprocess.run(["cmd", "/c", "dir"])

# System Information (equivalent to uname -a)
print('Gathering system information...')
subprocess.run(["cmd", "/c", "systeminfo"])

# Active processes (equivalent to ps -x)
print('Gathering active process information...')
subprocess.run(["cmd", "/c", "tasklist"])
