import nmap
import datetime
import time

# Network scanner function return the 2 list of MAC and IP addresses
def scanner(nm, sadd = '192.168.1.0/24'):
    mac = []
    ip = []
    vend = {}
    nm.scan(hosts=sadd, arguments='-sP')
    for h in nm.all_hosts():
        if 'mac' in nm[h]['addresses']:
            mac.append(nm[h]['addresses']['mac'])
            ip.append(nm[h]['addresses']['ipv4'])
            vend.update(nm[h]['vendor'])
    return ip, mac, vend

# Function for printing the net table
def printer(ip, mac, vend):
    i=0
    print '-------------------------------------------------------------'
    print '|      IP      |      MAC addrs      |        Vendor        |'
    print '-------------------------------------------------------------'
    for k in mac:
        if k in vend:
            print ' %s\t%s\t%s' % (ip[i], k, vend[k])
        else:
            print ' %s\t%s' % (ip[i], k)
        i=i+1
# Function for printing the net table
def fprinter(f, ip, mac, vend):
    i=0
    for k in mac:
        if k in vend:
            f.write(ip[i] + '  ' + k + '  ' + vend[k] + '\n')
        else:
            f.write(ip[i] + '  ' + k + '\n')
        i=i+1

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
f = open('database.txt', 'w')
printer(ip,mac,vend) # Calling print function
fprinter(f,ip,mac,vend) # Calling print on file function
