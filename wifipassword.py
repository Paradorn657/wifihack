import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp874').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('Latin-1').split('\n')

    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    print("{} | พาสเวิร์ด {}".format(i,results))