dev1 = {}  # method 2
dev1 = {"ip":"10.3.21.5", "version":"A.01.01",  "username":"user1","password":"pw1"}

ip_address = dev1['ip']  # get IP address
dev1['OS'] = 'NX-OS'         # add new field for 'OS'
dev1['version'] = 'a.01.12'  # modify version number
del dev1['OS']   # delete item located at 'OS'

if 'OS' in dev1:
# take whatever action you desire

dev2 = dev1
dev2 = dev1.copy()

from copy import deepcopy
dev2 = deepcopy(dev1)

#List of Dictionaries 
#--------------------
# Create three dictionaries holding device information for specific devices
dev30 = {'name':'xrv-0','ip':'10.1.1.30','user':'cisco'}
dev31 = {'name':'xrv-1','ip':'10.1.1.31','user':'cisco'}
dev32 = {'name':'xrv-2','ip':'10.1.1.32','user':'cisco'}

# Create a list to hold information about all of my devices created above
dev_list = [i for i in range(3)]
dev_list[0] = dev30 # sets list item 0 to dictionary dev30
dev_list[1] = dev31 # sets list item 1 to dictionary dev31
dev_list[2] = dev32 # sets list item 2 to dictionary dev32

#or

dev_list = []
dev_list.append(dev30) # sets list item 0 to dictionary dev30
dev_list.append(dev31) # sets list item 1 to dictionary dev31
dev_list.append(dev32) # sets list item 2 to dictionary dev32

#Dictionary of Dictionaries 
#---------------------------
dev30 = {'ip':'10.1.1.30','user':'cisco'}
dev31 = {'ip':'10.1.1.31','user':'cisco'}
dev32 = {'ip':'10.1.1.32','user':'cisco'}
devices = {}
devices['xrv-0'] = dev30 # sets item 'xrv-0' to dev30
devices['xrv-1'] = dev31 # sets item 'xrv-1' to dev31
devices['xrv-2'] = dev32 # sets item 'xrv-2' to dev32

#Dictionary of Lists of Dictionaries
#-----------------------------------
# Create dictionaries holding device information for these three XRv devices
dev30 = {'name':'xrv-0','ip':'10.1.1.30','user':'cisco'}
dev31 = {'name':'xrv-1','ip':'10.1.1.31','user':'cisco'}
dev32 = {'name':'xrv-2','ip':'10.1.1.32','user':'cisco'}
# Creat a list for our XRv devices that we have just defined
xrv_devices = {}
xrv_devices.append(dev30) 
xrv_devices.append(dev31)
xrv_devices.append(dev32) 
all_devices = {'xrv':xrv_devices,  # all XRv devices go here
'nx-os':nx_devices, # all NX devices go here
'ios':ios_devices}  # all IOS devices go here


