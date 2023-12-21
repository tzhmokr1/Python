# Connect to device and RegEX
import pexpect
from pprint import pprint
import re

# Print heading
print ''
print 'Interfaces, routes list, routes details'
print '---------------------------------------'

# Create regular expressions to match interfaces and OSPF
OSPF_pattern = re.compile('^O')
intf_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9])')

# Create regular expressions to match prefix and routes
prefix_pattern = re.compile('^O.{8}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})')
route_pattern = re.compile('via ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

# Connect to device and run 'show ip route' command
print '--- connecting telnet 10.30.30.1 with cisco/cisco'

session = pexpect.spawn('telnet 10.30.30.1', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for failure
if result != 0:
    print 'Timeout or unexpected reply from device'
    exit()

# Successfully got username prompt, enter username
session.sendline('cisco')
result = session.expect('Password:')

# Enter password
session.sendline('cisco')
result = session.expect('>')


# Read the route information using show ip route



# Must set terminal length to zero for long replies
print '--- setting terminal length to 0'
session.sendline('terminal length 0')
result = session.expect('>')

# Run the 'show ip route' commanmd on device
print '--- successfully logged into device, performing show ip route command'
session.sendline('show ip route')
result = session.expect('>')

# Print out the output of the command, for comparison
print '--- show ip route output:'
show_ip_route_output = session.before
print show_ip_route_output

# Get the output from the command into a list of lines from the output
routes_list = show_ip_route_output.splitlines()

# Create a list of OSPF routes using the output of the show ip route command

intf_routes= {} # Create dictionary to hold number of routes per interface

# Go through the list of routes to get routes per interface
for route in routes_list:

    OSPF_match = OSPF_pattern.search(route)
    if OSPF_match:

        intf_match = intf_pattern.search( route ) # Match for Gigabit Ethernet

        # Check to see if we matched the Gig Ethernet string
        if intf_match:

            intf = intf_match.group(2) # get the interface from the match


# For every route created above, create a dictionary holding the destination IP address/subnet, and the next hop.

if intf not in intf_routes: # If route list not yet created, do so now
                intf_routes[intf] = []

            # Extract the prefix (destination IP address/subnet)
            prefix_match = prefix_pattern.search(route)
            prefix = prefix_match.group(1)

            # Extract the route
            route_match = route_pattern.search(route)
            next_hop = route_match.group(1)

            # Create dictionary for this route, and add it to the list
            route = {'prefix':prefix,'next-hop':next_hop}
            intf_routes[intf].append(route)


pprint(intf_routes)
print '' # Print final blank line
