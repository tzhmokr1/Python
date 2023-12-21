util.py

import csv
from pprint import pprint

from devclass import NetworkDevice
from devclass import NetworkDeviceIOS

import logging

#======================================================================
def read_devices_info(devices_file):

    devices_list = []

    logging.info('util: reading device info from file: %s', devices_file)

    file = open(devices_file,'r')   # Open the CSV file
    csv_devices = csv.reader(file)  # Create the CSV reader for file

    # Use list comprehension to put CSV data into list of lists
    return [dev_info for dev_info in csv_devices]

#====================================================================
def print_device_info(device):

    print '-------------------------------------------------------'
    print '    Device Name:      ',device.name
    print '    Device IP:        ',device.ip_address
    print '    Device username:  ',device.username,
    print '    Device password:  ',device.password
    print '-------------------------------------------------------'

#====================================================================
def write_devices_info(devices_file, devices_out_list):

    logging.info('util: writing device info to file: %s', devices_file)

    # Use CSV library to output our list of lists to a CSV file
    with open(devices_file, 'w') as file:
        csv_out = csv.writer(file)
        csv_out.writerows(devices_out_list)
