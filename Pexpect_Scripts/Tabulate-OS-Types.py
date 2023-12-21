from pprint import pprint

# Print heading
print('')
print('Counts of different OS-types for all devices')
print('============================================')

os_types = { 'Cisco IOS':    {'count':0, 'devs':[] },
             'Cisco Nexus':  {'count':0, 'devs':[] },
             'Cisco IOS-XR': {'count':0, 'devs':[] },
             'Cisco IOS-XE': {'count':0, 'devs':[] } }

file = open("kris.txt","r")
for line in file:
    device_info_list = line.strip().split(",")
    device_info = {}
    device_info["name"] = device_info_list[0]
    device_info["os-type"] = device_info_list[1]
    name = device_info["name"]
    os = device_info["os-type"]

    if os == "ios":
        os_types["Cisco IOS"]["count"] += 1
        os_types["Cisco IOS"]["devs"].append(name)
    elif os == "nx-os":
        os_types["Cisco Nexus"]["count"] += 1
        os_types["Cisco Nexus"]["devs"].append(name)
    elif os == "ios-xr":
        os_types["Cisco IOS-XR"]["count"] += 1
        os_types["Cisco IOS-XR"]["devs"].append(name)
    elif os == "ios-xe":
        os_types["Cisco IOS-XE"]["count"] += 1
        os_types["Cisco IOS-XE"]["devs"].append(name)
    else:
        print("Warning: unknown device type:", os)
    
        
pprint(os_types)
file.close()

