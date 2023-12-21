
dev_os_types = {'ios','xr','nx'}

devices_list = ['xr','nx','nx','xe','xr','nx','xr','ios','nx','xe','xr','xr','nx']
dev__os_types = set(device_types_list)
if 'ios' in dev_os_types:
 # do something with ios devices

dev_types = set()
dev_types.add('crs') # add device type 'crs' to set
dev_types.update(['isr','asr']) # add more device types
dev_types.remove('crs')  # remove device type 'crs'

ip = '10.3.21.17'
used_ip_addresses = {'10.3.21.1','10.3.21.2','10.3.21.3', '10.2.21.4','10.3.21.5'}
if ip in used_ip_addresses # test if 'ip' is used yet
