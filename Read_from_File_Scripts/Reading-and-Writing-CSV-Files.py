import csv
from pprint import pprint
import pexpect

#---- Class to hold information about a generic network device --------
class NetworkDevice():

    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'

#---- Class to hold information about an IOS network device --------
class NetworkDeviceIOS(NetworkDevice):

    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)

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







#= Functions ================================================================
def read_devices_info(devices_file):

    devices_list = []

    file = open("devices_file",'r')   # Open the CSV file
    csv_devices = csv.reader(file)  # Create the CSV reader for file

    # Iterate through all devices in our CSV file
    for device_info in csv_devices:

        # Create a device object with this data
        if device_info[1] == 'ios':
 
            device = NetworkDeviceIOS(device_info[0],device_info[2],
                                      device_info[3],device_info[4])

        elif device_info[1] == 'ios-xr':
 
            device = NetworkDeviceXR(device_info[0],device_info[2],
                                     device_info[3],device_info[4])

        else:
            device = NetworkDevice(device_info[0],device_info[2],
                                   device_info[3],device_info[4])

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

    print('---- Printing CSV output ------------------------------')

    # Create the list of lists with devices and device info
    devices_out_list = []  # create list for CSV output

    for device in devices_list:
        dev_info = [device.name,device.ip_address,device.interfaces != ""]
        devices_out_list.append(dev_info)
 
    pprint(devices_out_list)

    # Use CSV library to output our list of lists to a CSV file
    with open("devices_file", 'w') as file:
        csv_out = csv.writer(file)
        csv_out.writerows(devices_out_list)









#====================================================================
# Main program: connect to device, show interface, display

devices_list = read_devices_info('csv-devices')  # read CSV info for all devices

for device in devices_list:

    print('==== Device =============================================================')

    device.connect()          # connect to this specific device
    device.get_interfaces()   # get interface info for this specific device

    print_device_info(device)   # print device details for this device

write_devices_info('csv-devices-out', devices_list)   # write CSV entry for all devices
