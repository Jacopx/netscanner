import nmap
import datetime
import time
import os
import netifaces # Package for network interface
from netaddr import IPAddress # Package for IP addresse
from prettytable import PrettyTable # Package for table

# Menu function
def menu(t):
    os.system('clear')
    now = datetime.datetime.now() #get time
    print ('Network Scanner by Jacopx -- ' + (now.strftime("%d/%m/%Y %H:%M")))
    print ('---------------------------------------------')
    print ('1. Simple Network Scan')
    print ('2. Net Database Comparison')
    print ('3. Showing Database')
    print ('4. Edit Database')
    print ('5. Clear Database')
    print ('9. EXIT')
    if t==1:
        try: # If NO input reprint the menu
            c=input('Choose: ')
            print ('---------------------------------------------')
            return c
        except:
            menu(1)
    else:
        print ('---------------------------------------------')

# The scanner function call the nmap package for scanning the network
def scanner(nm):
    mac = []; ip = []; vend = []; htname=[]; i=0
    add=netifaces.ifaddresses('en5')
    sadd = '%s/%d' % (add[netifaces.AF_INET][0]['addr'], IPAddress(add[netifaces.AF_INET][0]['netmask']).netmask_bits())

    print ("Your Network is: " + sadd)
    nm.scan(hosts=sadd, arguments='-sP')

    for h in nm.all_hosts():
        # If NMAP get the MAC...
        if 'mac' in nm[h]['addresses']:
            mac.append(nm[h]['addresses']['mac'])
        else:
            mac.append('XX:XX:XX:XX:XX:XX')

        # The IPv4 address
        ip.append(nm[h]['addresses']['ipv4'])

        # If NMAP get the Host name...
        if nm[h]['hostnames'][0]['name']!="":
            htname.append(nm[h]['hostnames'][0]['name'])
        else:
            htname.append('----')

        # If NMAP get the Vendor name...
        if mac[-1] in nm[h]['vendor']:
            vend.append(nm[h]['vendor'][mac[-1]])
        else:
            vend.append('----')

    return ip, mac, vend, htname # Return all list

# Function for printing the net table
def printer(ip, mac, vend, name):
    # Table Header
    t = PrettyTable(['IP', 'MAC addrs', 'Host Name', 'Vendor'])

    # Adding row in the table
    for i in range(len(mac)):
        t.add_row([ip[i], mac[i], name[i], vend[i]])

    # Print the table
    print (t)

def dbprinter(typ, ip, mac, vend, name):
    # Table Header
    t = PrettyTable(['Type', 'IP', 'MAC addrs', 'Host Name', 'Vendor'])

    # Adding row in the table
    for i in range(len(mac)):
        t.add_row([typ[i], ip[i], mac[i], name[i], vend[i]])

    # Print the table
    print (t)

# Function for printing the net table in file
def fprinter(f, typ, ip, mac, vend, name):
    for i in range(len(mac)):
        if typ[i]=="NEW":
            f.write(ip[i] + ',' + mac[i] + ',' + name[i] + ',' + vend[i] + '\n')

def show_file(f):
    # Declaring all lists
    entry = []; fip=[]; fmac=[]; fvend=[]; fname=[]

    # For each line in file
    for line in f:
        entry=line.split(',')
        fip.append(entry[0])
        fmac.append(entry[1])
        fname.append(entry[2])
        if len(entry)>3:
            fvend.append(entry[3])

    f.close()

    # Return all data
    return fip, fmac, fvend, fname

def checkf(f, ip, mac, vend):
    # Declaring all lists
    typ = []; entry = []; fip=[]; fmac=[]; fvend=[]

    # For each line in file
    for line in f:
        entry=line.split(',')
        fip.append(entry[0])
        fmac.append(entry[1])
        if len(entry)>3:
            fvend.append(entry[3])

    # Check if is a NEW or an already KNOW device
    for k in mac:
        if k in fmac:
            typ.append('KNOW')
        else:
            typ.append('NEW')
    f.close()

    return typ
