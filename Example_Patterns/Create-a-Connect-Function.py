import pexpect

#-----------------------------------------------------------
# The following code connects to a device

def connect(dev_ip,username,password):
    """
    Connects to device using pexpect

    :dev_ip: The IP address of the device we are connectin to
    :username: The username that we should use when logging in
    :password: The password that we should use when logging in

    =return: pexpect session object if succssful, 0 otherwise

    """

    print('--- attempting to: telnet ' + dev_ip)

    session = pexpect.spawn('telnet ' + dev_ip, timeout=20)

    result = session.expect(['Username:', pexpect.TIMEOUT])
    # Check for failure
    if result != 0:
        print('--- Timeout or unexpected reply from device')
        return 0

    print('--- attempting to: username: ' + username)

    # Successfully got username prompt, logging with username
    session.sendline(username)

    result = session.expect(['Password:', pexpect.TIMEOUT])
    # Check for failure
    if result != 0:
        print('--- Timeout or unexpected reply from device')
        return 0

    print('--- attempting to: password: ' + password)

    # Successfully got password prompt, logging in with password
    session.sendline(password)
    session.expect('>')

    return session  # return pexpect session object to caller


#-----------------------------------------------------------
# The following function gets and returns interface information

def show_int_summary(session):
    """
    Runs 'show int summary' command on device and returns 
    output from device in a string

    :session: The pexpect session for communication with device

    =return: string of output from device
    """

    print('--- show interface summary command')
    session.sendline('show interface summary')
    result = session.expect('>')

    print('--- getting interface command output')
    show_int_brief_output = session.before

    return show_int_brief_output



#------------------------------------------------------------
# Main program: connect to device, show interface, display

if __name__ == '__main__':

    session = connect('10.30.30.1','cisco','cisco')
    if session == 0:
        print('--- Session attempt unsuccessful, exiting.')
        exit()

    output_data = show_int_summary(session)

    print('')
    print('Show Interface Output')
    print('-----------------------------------------------------')
    print('')

    print(output_data)

    session.sendline('quit')
    session.kill(0)









