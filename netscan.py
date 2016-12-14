import nmap
import datetime
import time
import os
import glob


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
            print ' %s\t %s\t%s' % (ip[i], k, vend[k])
        else:
            print ' %s\t %s' % (ip[i], k)
        i=i+1
# Function for printing the net table
def fprinter(f, ip, mac, vend):
    i=0
    for k in mac:
        if k in vend:
            f.write(ip[i] + ',' + k + ',' + vend[k] + '\n')
        else:
            f.write(ip[i] + ',' + k + '\n')
        i=i+1

# START SCRIPT WITH MENU
c=0
while c!=9:
    now = datetime.datetime.now() #get time
    print '\nNetwork Scanner by Jacopx -- ' + (now.strftime("%d/%m/%Y %H:%M"))
    print '---------------------------------------------'
    print '1. Simple Network Scan'
    print '2. Net Database Comparison'
    print '3. Showing Database'
    print '4. Edit Database'
    print '5. Clear Database'
    print '9. EXIT'
    c=input('Choose: ')
    print '---------------------------------------------'

    if c==1: # Simple Network Scan
        # Network Informations
        sc_add = raw_input('Address/Netmask(PL): ')
        nm = nmap.PortScanner()
        # Call scan function
        if len(sc_add) == 0:
            ip, mac, vend = scanner(nm) # Function call for scan default network 192.168.1.0/24
        else:
            ip, mac, vend = scanner(nm, sc_add) # Function call for scan network host insert by user
        printer(ip,mac,vend) # Calling print function
        c=input('Back to home (1): ')
        if c==1:
            os.system('clear')
            continue
        else:
            raise SystemExit
    elif c==2:
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        netname = raw_input('Insert the Network Name: ')
        netname = 'database/%s' % (netname)
        f=open(netname, 'rw')
        print f
    # elif c==3:
    #
    # elif c==4:

    elif c==9:
        print 'Goodbye!'
        raise SystemExit
    print '---------------------------------------------'
