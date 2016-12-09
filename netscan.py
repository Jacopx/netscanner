import nmap
import datetime
import time

# Network scanner function return the 2 list of MAC and IP addresses
def scanner(nm, sadd = '192.168.1.0/24'):
    mac = []
    ip = []
    vend = []
    nm.scan(hosts=sadd, arguments='-sP')
    for h in nm.all_hosts():
        if 'mac' in nm[h]['addresses']:
            mac.append(nm[h]['addresses']['mac'])
            ip.append(nm[h]['addresses']['ipv4'])
            if nm[h]['vendor'].iteritems()>0:
                vend.append(nm[h]['vendor'].values())
            else:
                vend.append('NOT RETRIVE')
    return ip, mac, vend

# Header of the software with time
now = datetime.datetime.now() #get time
print '\nNetwork Scanner by Jacopx -- ' + (now.strftime("%d/%m/%Y %H:%M"))
print '---------------------------------------------'

# Network Informations
sc_add = raw_input('Address/Netmask(PL): ')
nm = nmap.PortScanner()

# Call scan function
if len(sc_add) == 0:
    ip, mac, vend = scanner(nm) # Function call for scan default network 192.168.1.0/24
else:
    ip, mac, vend = scanner(nm, sc_add) # Function call for scan network host insert by user

for i in range(0,len(mac)):
    print '%s\t%s\t%s' %(ip[i], mac[i], vend[i])
