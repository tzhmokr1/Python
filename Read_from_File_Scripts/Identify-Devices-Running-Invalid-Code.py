from pprint import pprint

current_version = 'Version 5.3.1'
device_info = {}

# Read all lines of device information from file
file = open('kris.txt',"r")
for line in file:
    device_info_list = line.strip().split(',') # Get device info into list
    device_info["name"] = device_info_list[0]
    device_info["os-type"] = device_info_list[1]
    device_info["ip"] = device_info_list[2]
    device_info["version"] = device_info_list[3]
    device_info["username"] = device_info_list[4]
    device_info["password"] = device_info_list[5]
    if device_info["version"] != current_version:
         print(("Device:  "), device_info["name"]), print(("Version: "), device_info["version"])
file.close()
