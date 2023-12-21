devices_list = [] # Create the outer list for all devices

# Read in the devices from the file
file = open('kris.txt','r')
line = file.readline()
while line :
    device_info_list = line.split(',') # Get device info into list
    device_info = {}
    device_info["name"] = device_info_list[0]
    device_info["os-type"] = device_info_list[1]
    device_info["ip"] = device_info_list[2]
    device_info["version"] = device_info_list[3]
    devices_list.append(device_info)
    line = file.readline()
file.close() # Close the file since we are done with it

print('')
print('Name     OS-type  IP address           Software         ')
print('------   -------  ------------------   ------------------')

index = 0
while index < len(devices_list):
    device = devices_list[index]
    print('{0:8} {1:8} {2:20} {3:20}'.format(device['name'],
                                             device['os-type'],
                                             device['ip'],
                                             device['version']))

    index += 1
print('')
