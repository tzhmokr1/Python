import pexpect

#-----------------------------------------------------------
def read_devices_info(filename):

    devices_list = []

    file = open(filename,'r')
    for line in file:

        device_info_list = line.strip().split(',')

        device_info = {}
        device_info['name'] = device_info_list[0]
        device_info['ip'] = device_info_list[1]
        device_info['username'] = device_info_list[2]
        device_info['password'] = device_info_list[3]

        devices_list.append(device_info)

    return devices_list



# The following code connects to a device

def connect(dev_ip,username,password):

    print '--- connecting IOS: telnet '+dev_ip

    session = pexpect.spawn('telnet ' + dev_ip, timeout=20)

    result = session.expect(['Username:', pexpect.TIMEOUT])
    # Check for failure
    if result != 0:
        print '--- Timeout or unexpected reply from device'
        return 0

    print '--- attempting to: username: ' + username

    # Successfully got username prompt, logging with username
    session.sendline(username)

    result = session.expect(['Password:', pexpect.TIMEOUT])
    # Check for failure
    if result != 0:
        print '--- Timeout or unexpected reply from device'
        return 0

    print '--- attempting to: password: ' + password

    # Successfully got password prompt, logging in with password
    session.sendline(password)
    session.expect('>')

    return session  # return pexpect session object to caller



# The following function gets and returns interface information

def show_int_summary(session):

    session.sendline('show interface summary')
    result = session.expect('>')

    show_int_summary_output = session.before

    return show_int_summary_output


# The following function prints device information

def print_device_info(device_info,show_int_output):

    print '-------------------------------------------------------'
    print '    Device Name:      ',device_info['name']
    print '    Device IP:        ',device_info['ip']
    print '    Device username:  ',device_info['username'],
    print '    Device password:  ',device_info['password']

    print ''
    print '    Show Interface Output'
    print ''

    print show_int_output
    print '-------------------------------------------------------'

# Main program: connect to device, show interface, display

if __name__ == '__main__':

    devices_list = read_devices_info('real-devices')

    for device_info in devices_list:

        session = connect(device_info['ip'],
                          device_info['username'],
                          device_info['password'])
        if session == 0:
            print '--- Session attempt unsuccessful ---'
            continue

        show_int_output = show_int_summary(session)

        print_device_info(device_info,show_int_output)

        session.sendline('quit')
        session.kill(0)
