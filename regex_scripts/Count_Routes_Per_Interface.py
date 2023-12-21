from pprint import pprint
inport re

gig_pattern = re.compile("(GigabitEthernet)([0-9])\/[0-9]\/[0-9]\/[0-9])")

routes = {}

file = open("routes.txt","r")
for line in file:
    match = gig_pattern.search(line)
    if match:
        intf = match.group(2)
        routes[intf] = routes[intf]+1 if intf in routes else 1
    else:
        continue
    
print('')
print('Number of routes per interface')
print('------------------------------')
pprint(routes)

