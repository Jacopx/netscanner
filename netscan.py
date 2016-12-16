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

def checkf(f, ip, mac, vend):
    know = []
    entry = []
    fip=[]
    fmac=[]
    fvend=[]
    for line in f:
        entry=line.split(',')
        fip.append(entry[0])
        fmac.append(entry[1])
        if len(entry)>2:
            fvend.append(entry[2])
    for k in mac:
        for j in fmac:
            if k==j:
                know.append(1)
            else:
                know.append(0)
    return know

def dbadd(f, ip, mac, vend, know):
    i=0
    for k in mac:
        if know[i]==0:
            if k in vend:
                f.write(ip[i] + ',' + k + ',' + vend[k] + '\n')
            else:
                f.write(ip[i] + ',' + k + '\n')
    print 'Host added!\n'

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
        new=0
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        netname = raw_input('Insert the Network Name: ')
        netname = 'database/%s.db' % (netname)
        try:
            f=open(netname, 'rb')
            print f
        except:
            print 'File opening faile!'
            print 'Creation of the new DB!'
            new=1
            f=open(netname, 'wb+')

        # Network Informations
        sc_add = raw_input('Address/Netmask(PL): ')
        nm = nmap.PortScanner()
        # Call scan function
        if len(sc_add) == 0:
            ip, mac, vend = scanner(nm) # Function call for scan default network 192.168.1.0/24
        else:
            ip, mac, vend = scanner(nm, sc_add)

        if new==1:
            fprinter(f,ip,mac,vend) # Calling print to file function
        else:
            know = checkf(f,ip,mac,vend) # Calling the checking batabase function
            i=0
            for k in mac:
                if know[i]==0:
                    if k in vend:
                        print 'New host: ' + k + ' ---> ' + ip[i] + '(' + vend[k] + ')'
                    else:
                        print 'New host: ' + k + ' ---> ' + ip[i]
                i=i+1
        m = input('Do you want to add this new host to the db (1): ')
        if m==1:
            dbadd(f, ip, mac, vend, know)
        else:
            print 'Host deleted!'
    # elif c==3:
    #
    # elif c==4:

    elif c==9:
        print 'Goodbye!'
        raise SystemExit
    print '---------------------------------------------'
