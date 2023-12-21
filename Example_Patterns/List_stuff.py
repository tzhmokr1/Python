device_tuple = ('10.3.21.5', 'username', 'password')
device_list = list(device_tuple)

device_string = '10.3.21.5 ,username, password'
device_list = device_string.split(',')

device_types = ['IOS','XR'] # create list
device_types.append('XE') # add 'XE' to list

device_types.insert(2,'NX') # insert 'NX' at index 2

device_list.remove('NX')  # remove item matching 'NX'

del device_list[1] # remove item at index 1

item = device_list.pop() # pop the last item off list

#########################################################

dev_list_2 = dev_list_1 #Assignement


from copy import copy
dev_list_2 = copy(dev_list_1)  #Shallow Copy (copy only the first level items)

from copy import deepcopy
complex_list_2 = deepcopy(complex_list_1) #Deep Copy

#########################################################

ios_devs = ['10.3.21.5','10.3.21.6','10.3.21.7']
nx_devs = ['10.4.30.2','10.3.21.58']
xr_devs = ['10.5.2.1','10.5.2.6','10.5.2.7']
all_devices = [ios_devs, nx_devs, xr_devs]

#########################################################

device_string = '  1.1.1.1, username  , password   '
info_list = list()  # create empty list
device_info = device_string.split(,)  # create list from device_string
for item in device_info:
    item = item.strip()  # strip white space from device
    info_list.append(item)  #add to info_list
    
