import datetime
import time
import os
import netifaces
from netaddr import IPAddress


def menu(t):
    os.system('clear')
    now = datetime.datetime.now() #get time
    print 'Network Scanner by Jacopx -- ' + (now.strftime("%d/%m/%Y %H:%M"))
    print '---------------------------------------------'
    print '1. Simple Network Scan'
    print '2. Net Database Comparison'
    print '3. Showing Database'
    print '4. Edit Database'
    print '5. Clear Database'
    print '9. EXIT'
    if t==1:
        try: # If NO input reprint the menu
            c=input('Choose: ')
            print '---------------------------------------------'
            return c
        except:
            menu(1)
    else:
        print '---------------------------------------------'
# Network scanner function return the 2 list of MAC and IP addresses
def scanner(nm):
    mac = []; ip = []; vend = []; i=0
    add=netifaces.ifaddresses('en0')
    sadd = '%s/%d' % (add[netifaces.AF_INET][0]['addr'], IPAddress(add[netifaces.AF_INET][0]['netmask']).netmask_bits())

    print "Your Network is: " + sadd
    nm.scan(hosts=sadd, arguments='-sP')
    for h in nm.all_hosts():
        if 'mac' in nm[h]['addresses']:
            mac.append(nm[h]['addresses']['mac'])
            ip.append(nm[h]['addresses']['ipv4'])
            if mac[-1] in nm[h]['vendor']:
                vend.append(nm[h]['vendor'][mac[-1]])
            else:
                vend.append('----')

    return ip, mac, vend

# Function for printing the net table
def printer(ip, mac, vend):
    i=0
    print '-------------------------------------------------------------'
    print '|      IP      |      MAC addrs      |        Vendor        |'
    print '-------------------------------------------------------------'

    for i in range(len(mac)):
        print ' %s\t %s\t%s' % (ip[i], mac[i], vend[i])

# Function for printing the net table
def fprinter(f, ip, mac, vend):
    for i in range(len(mac)):
        f.write(ip[i] + ',' + mac[i] + ',' + vend[i] + '\n')

def show_file(f):
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

    f.close()
    return fip, fmac, fvend

def checkf(f, ip, mac, vend):
    know = []
    entry = []
    fip=[]
    fmac=[]
    fvend=[]
    flag=0

    for line in f:
        entry=line.split(',')
        fip.append(entry[0])
        fmac.append(entry[1])
        if len(entry)>2:
            fvend.append(entry[2])

    for k in mac:
        if k in fmac:
            know.append(1)
            flag=1
        else:
            know.append(0)
    f.close()
    return know, flag

def dbadd(f, ip, mac, vend, know):
    i=0
    for k in mac:
        if know[i]==0:
            if k in vend:
                f.write(ip[i] + ',' + k + ',' + vend[k] + '\n')
            else:
                f.write(ip[i] + ',' + k + ','+ '---\n')
        i=i+1
    f.close()
    print 'Host added!\n'
