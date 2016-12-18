import datetime
import time
import os

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
        c=input('Choose: ')
        print '---------------------------------------------'
        return c
    else:
        print '---------------------------------------------'
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

    for i in range(0,len(fmac)):
        if len(fvend[i])>0:
            print ' %s\t %s\t%s' % (fip[i], fmac[i], fvend[i])
        else:
            print ' %s\t %s' % (fip[i], fmac[i])
    f.close()

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
        if k in fmac:
            know.append(1)
        else:
            know.append(0)
    f.close()
    return know

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
