#!/usr/bin/env python

"""
Example of a script that executes a CLI command on a remote
device over established SSH connection.

Administrator login options and CLI commands are device specific,
thus this script needs to be adapted to a concrete device specifics.
Current script assumes interaction with Cisco IOS device.

NOTES: Requires installation of the 'paramiko' Python package: 
pip install paramiko
       The 'paramiko' package is documented at: 
http://docs.paramiko.org
       Complete set of SSH client operations is available at:
http://docs.paramiko.org/en/1.15/api/client.html

command_ssh.py
"""

# built-in modules
import time
import socket

# third-party modules
import paramiko

def enable_privileged_commands(device_info, rsh):

    """Turn on privileged commands execution.
    :param dict device_info: dictionary containing information
        about target device.
    :param paramiko.channel.Channel rsh: channel connected to a remote shell.
    """

    cmd = "enable\n"
    # Execute the command (wait for command to complete)
    rsh.send(cmd)
    time.sleep(1)
    output = rsh.recv(device_info['max_bytes'])
    if(device_info['password_prompt'] in output):
        password = "%s\n" % device_info['password']
        rsh.send(password)
        rsh.recv(device_info['max_bytes'])
