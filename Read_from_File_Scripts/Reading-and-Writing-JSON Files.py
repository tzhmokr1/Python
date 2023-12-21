import json
from pprint import pprint
import pexpect

#---- Class to hold information about a generic network device --------
class NetworkDevice():

    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.os_type = None

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'

#---- Class to hold information about an IOS network device --------
class NetworkDeviceIOS(NetworkDevice):

    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)
        self.os_type = 'ios'

    def connect(self):
        print('--- connecting IOS: telnet '+self.ip_address)

        self.session = pexpect.spawn('telnet '+self.ip_address, timeout=20)
        result = self.session.expect(['Username:', pexpect.TIMEOUT])

        self.session.sendline(self.username)
        result = self.session.expect('Password:')

        # Successfully got password prompt, logging in with password
        self.session.sendline(self.password)
        self.session.expect('>')
 
    def get_interfaces(self):
        
        self.session.sendline('show interfaces summary')
        result = self.session.expect('>')

        self.interfaces = self.session.before


#---- Class to hold information about an IOS-XR network device --------
class NetworkDeviceXR(NetworkDevice):

    #---- Initialize --------------------------------------------------
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)
        self.os_type = 'ios-xr'

    #---- Connect to device -------------------------------------------
    def connect(self):

        print('--- connecting XR: ssh '+self.username+'@'+self.ip_address)

        self.session = pexpect.spawn('ssh '+self.username+
                                     '@'+self.ip_address, timeout=20)
        result = self.session.expect(['password:', pexpect.TIMEOUT])

        # Check for failure
        if result != 0:
            print('--- Timout or unexpected reply from device')
            return 0

        # Successfully got password prompt, logging in with password
        print('--- password:',self.password)
        self.session.sendline(self.password)
        self.session.expect('#')

    #---- Get interfaces from device ----------------------------------
    def get_interfaces(self):

        self.session.sendline('show interface brief')
        result = self.session.expect('#')

        self.interfaces = self.session.before






#== Functions ==============================================================
def read_devices_info(devices_file):

    devices_list = []

    # Open the device file with JSON data and read into string
    json_file = open("devices_file",'r')   # open the JSON file
    json_device_data = json_file.read()  # read in the JSON data from file

    # Convert JSAON string into Python data structure
    devices_info_list = json.loads(json_device_data)

    for device_info in devices_info_list:

        # Create a device object with this data
        if device_info['os'] == 'ios':
 
            device = NetworkDeviceIOS(device_info['name'],device_info['ip'],
                                      device_info['user'],device_info['password'])

        elif device_info['os'] == 'ios-xr':
 
            device = NetworkDeviceXR(device_info['name'],device_info['ip'],
                                     device_info['user'],device_info['password'])

        else:
            device = NetworkDevice(device_info['name'],device_info['ip'],
                                   device_info['user'],device_info['password'])

        devices_list.append(device) # Append this device object to list

    return devices_list



#====================================================================
def print_device_info(device):

    print('-------------------------------------------------------')
    print('    Device Name:      ',device.name)
    print('    Device IP:        ',device.ip_address)
    print('    Device username:  ',device.username,)
    print('    Device password:  ',device.password)
    print('-------------------------------------------------------')

#====================================================================
def write_devices_info(devices_file, devices_list):

    print('---- Printing JSON output ------------------------------')

    # Create the list of lists with devices and device info
    devices_out_list = []  # create list for JSON output

    for device in devices_list:
        dev_info = {'name':device.name,'ip':device.ip_address,'os':device.os_type,
                    'user':device.username,'password':device.password}
        devices_out_list.append(dev_info)
 
    pprint(devices_out_list)

    # Convert the python device data into JSON for output to file
    json_device_data = json.dumps(devices_out_list)

    # Output the JSON string to a file
    with open("devices_file", 'w') as json_file:
        json_file.write(json_device_data)





#====================================================================
# Main program: connect to device, show interface, display

devices_list = read_devices_info('json-devices')  # read JSON info for all devices

for device in devices_list:

    print('==== Device =============================================================')

    device.connect()          # connect to this specific device
    device.get_interfaces()   # get interface info for this specific device

    print_device_info(device)   # print device details for this device

write_devices_info('json-devices-out', devices_list)   # write JSON entry for all devices

# Do it again, reading from our output file, to prove we did it correctly

print('-----------------------------------------------------------------------------')
print('---------- Reading from our output file, doing it again ---------------------')

devices_list = read_devices_info('json-devices-out')  # read JSON info for all devices

for device in devices_list:

    print('==== Device =============================================================')

    device.connect()          # connect to this specific device
    device.get_interfaces()   # get interface info for this specific device

    print_device_info(device)   # print device details for this device

