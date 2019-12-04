import subprocess, platform

print(platform.system())

if platform.system() == "Windows":
    cmd = "ping 8.8.8.8"
    returned_value = subprocess.call(cmd, shell=True)
    print("returned_value: ", returned_value)