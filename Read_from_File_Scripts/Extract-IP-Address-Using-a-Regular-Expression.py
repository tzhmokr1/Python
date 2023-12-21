from pprint import pprint
import re

ip_addr_pattern = re.compile('Mgmt:([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

file = open("kris.txt","r")
for line in file:
    device_info_list = line.strip().split(",")
    device_info = {}
    device_info["name"] = device_info_list[0]
    mgmt_addr = ip_addr_pattern.search(line)
    device_info["ip"] = mgmt_addr.group(1)
    print(("Device: "),device_info["name"])
    print(("MgmtIP: "),device_info["ip"])
file.close()
