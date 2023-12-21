devclass.py

import pexpect
import logging

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
        self.interfaces = '--- Base Device, does not know how to get interfaces'

#==== Class to hold information about an IOS network device ==================
class NetworkDeviceIOS(NetworkDevice):

    #---------------------------------------------------------------------------
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)
        logging.info('devclass: created IOS device: %s %s', name, ip)

#---------------------------------------------------------------------------
    def connect(self):
        print '--- connecting IOS: telnet: '+self.username+'/'+self.password

        self.session = pexpect.spawn('telnet '+self.ip_address, timeout=20)
        result = self.session.expect(['Username:', pexpect.TIMEOUT, pexpect.EOF])

        # Check for failure
        if result != 0:
            logging.warn('devclass: --- Timout or unexpected reply from device')
            return 0

        # Successfully got username prompt, logging in with password
        self.session.sendline(self.username)
        result = self.session.expect(['Password:', pexpect.TIMEOUT])

        # Check for username failure
        if result != 0:
            logging.warn(
                'devclass: --- Timeout or unexpected username reply from device')
            return 0

        # Successfully got password prompt, finish log in with password
        self.session.sendline(self.password)
        result = self.session.expect(['>', 'invalid', pexpect.TIMEOUT])

        # Check for password failure
        if result != 0:
            logging.warn(
                'devclass: --- Timeout or unexpected password reply from device')
            return 0

        logging.info('devclass: successful login at: %s for user: %s',
                                                   self.ip_address,self.username)

        return self.session

    #---------------------------------------------------------------------------
    def set_terminal_length(self):

        # Must set terminal length to zero for long replies
        self.session.sendline('terminal length 0')
        result = self.session.expect(['>', pexpect.TIMEOUT])

        if result != 0:
            logging.warn('devclass: --- Timeout or unexpected reply')
            return False

        else: return True

 
    #---------------------------------------------------------------------------
    def get_interfaces(self):
        
        self.session.sendline('show interfaces summary')
        result = self.session.expect(['>', pexpect.TIMEOUT])

        print 'show interfaces summary result: ',result

        if result != 0:
            logging.warn('--- Timeout or unexpected reply from show interfaces')
            return 0

        self.interfaces = self.session.before
        return self.interfaces

    #---------------------------------------------------------------------------
    def get_routes(self):
        
        self.session.sendline('show ip route')
        result = self.session.expect(['>', pexpect.TIMEOUT])

        print 'show interfaces summary result: ',result

        if result != 0:
            logging.warn('--- Timeout or unexpected reply from show interfaces')
            return 0

        self.interfaces = self.session.before
        return self.interfaces
