import nmap
import datetime
import time
import os
import glob
from netf import *

# START SCRIPT WITH MENU
c=0
while c!=9:
    c=menu(1)
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
        know=[]
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        netname = raw_input('Insert the Network Name: ')
        netname = 'database/%s.db' % (netname)
        try:
            fr=open(netname, 'r')
            fa=open(netname, 'a')
            menu(0)
            print fr, fa
        except:
            print 'File opening faile!'
            print 'Creation of the new DB!'
            new=1
            f=open(netname, 'w+')

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
            know = checkf(fr,ip,mac,vend) # Calling the checking batabase function
            i=0
            nn=0
            for k in mac:
                if know[i]==0:
                    nn=1
                    if k in vend:
                        print 'New host: ' + k + ' ---> ' + ip[i] + ' (' + vend[k] + ')'
                    else:
                        print 'New host: ' + k + ' ---> ' + ip[i]
                i=i+1
        if nn==0:
            print 'No new hosts'
            c=input('Back to home: ')
            os.system('clear')
        else:
            m = input('Do you want to add this new host to the db (1): ')
            if m==1:
                dbadd(fa, ip, mac, vend, know)
            else:
                print 'Host deleted!'

        os.system('clear')
    elif c==5:
        os.system('clear')
        menu(0)
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        dbdel = raw_input('Insert the Network Name to delete: ')
        dbdel = 'rm database/%s.db' % (dbdel)
        os.system(dbdel)
    elif c==9:
        print 'Goodbye!'
        raise SystemExit
    print '---------------------------------------------'
