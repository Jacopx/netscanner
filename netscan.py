import nmap
import datetime
import time

# addr = raw_input('Insert the host to be scanned: ')
# netmask = raw_input('Insert the netmask (prefix length): ')

nm = nmap.PortScanner()
nm.scan(hosts='192.168.1.0/24', arguments='-sL')
for h in nm.all_hosts():
    if 'mac' in nm[h]['addresses']:
        print(nm[h]['addresses'], nm[h]['vendor'])
