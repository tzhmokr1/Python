devices_list = [] # Create the outer list for all devices

print('')
print('Idx Name     OS-type  IP address           Software            ')
print('--- -------- -------- -------------------- --------------------')

index = 0

# Read in the devices from the file
file = open('kris.txt','r')
for line in file:
    device_info = line.split(',') # Get device info into list
    devices_list.append(device_info)
    print('{0:2}: {1:8} {2:8} {3:20} {4:20}'.format(index+1,
                                                    device_info[0],device_info[1],
                                                    device_info[2],device_info[3]))
    index += 1 # increment our index
file.close() # Close the file since we are done with it
print('')


while True: # Loop forever, until user terminates program

    # Request user to input the IP address we will search for
    try:
        ip_address = input('Enter device IP address to find (Ctrl-C to exit):')
    except KeyboardInterrupt:
        break;

    # Loop through our devices looking for a match on IP address
    for index in range(0, len(devices_list)):

        device_info = devices_list[index] # Get information for this device in the list
        if device_info[2][9:] == ip_address:  # Check to see if device IP is a match

            # If a match, print results and stop looking
            print('{0:2}: {1:8} {2:8} {3:20} {4:20}'.format(index+1,
                                                     device_info[0],device_info[1],
                                                     device_info[2],device_info[3]))
            break
        else:
            continue

    else:  # We get here if we exhausted the device list, IP not found
        print('--- Given IP address not found ---')

print('\n')
print('Device search terminated.\n')

