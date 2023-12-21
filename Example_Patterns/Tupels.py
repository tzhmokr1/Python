dev_info = ('iosxrv1', 'A.01.01')
version = dev_info[1]

device_tuple = ('1.1.1.1','username','password')
device_list = list(my_tuple)

device_tuple = ('1.1.1.1','username','password')
ip, user, pw = device_tuple

from collections import namedtuple
Info = namedtuple('Info','name version')
dev_info = Info(name='iosxrv1', version='A.01.01')
version = dev_info.version
