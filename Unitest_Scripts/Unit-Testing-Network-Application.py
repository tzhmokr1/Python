import unittest
import filecmp
from pprint import pprint

import util

csv_test_input_filename  = 'csv-in-test-devices'
csv_test_output_filename = 'csv-out-test-devices'

# Input file for testing. Note the '\r\n', required for file comparison test.
csv_input_file_string = \
         ('test-1,test-os,1.1.1.1,test-username1,test-password1\r\n'
          'test-2,test-os,1.1.1.2,test-username2,test-password2\r\n'
          'test-3,test-os,1.1.1.3,test-username3,test-password3\r\n'
          'test-4,test-os,1.1.1.4,test-username4,test-password4\r\n')
print '---- CSV Test Devices Input String ----------------------------------'
pprint(csv_input_file_string)

# Devices list for comparison - this is the data that should be created
# when the file above is read by our code under test.
csv_test_devices_list = \
         [['test-1','test-os','1.1.1.1','test-username1','test-password1'],
          ['test-2','test-os','1.1.1.2','test-username2','test-password2'],
          ['test-3','test-os','1.1.1.3','test-username3','test-password3'],
          ['test-4','test-os','1.1.1.4','test-username4','test-password4']]
print '---- CSV Test Devices List ------------------------------------------'
pprint(csv_test_devices_list)
