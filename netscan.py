import nmap
import datetime
import time
import os
import glob
from netf import *
import netifaces

# START SCRIPT WITH MENU
c=0
while c!=9:
    c=menu(1)
    if c==1: # Simple Network Scan

        nm = nmap.PortScanner() # Calling NMAP function
        ip, mac, vend = scanner(nm) # Call function for scan
        printer(ip,mac,vend) # Calling print function
        c=input('Back to home (1): ')
        if c==1:
            os.system('clear')
            continue
        else:
            raise SystemExit

    elif c==2:
        # Declaring Variable
        new=0; know=[]
        # Showing all database
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        netname = raw_input('Insert the Network Name: ')
        netname = 'database/%s.db' % (netname)
        try: # Try to open the files, the first for checking the database, the second for appending the net hosts
            fr=open(netname, 'r')
            fa=open(netname, 'a')
            menu(0)
        except: # If there is no database, create it!
            menu(0)
            print 'File opening failed!'
            print 'Creation of the new DB!'
            new=1
            f=open(netname, 'w+')

        # Call scan function
        nm = nmap.PortScanner()
        ip, mac, vend = scanner(nm) # Function call for your network

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
    elif c==3:

        os.system('clear')
        menu(0)
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        show = raw_input('Insert the Network Name to show: ')
        show = 'database/%s.db' % (show)
        try: # Try to open the database
            fr=open(show, 'r')
            ip, mac, vend = show_file(fr)
            printer(ip, mac, vend)
        except:
            print "Open failed!"

        c=input('Back to home (1): ')
        if c==1:
            os.system('clear')
            continue
        else:
            raise SystemExit

    elif c==5:

        os.system('clear')
        menu(0)
        db=glob.glob('database/*.db')
        for net in db:
            print '/%s' % (net)
        dbdel = raw_input('Insert the Network Name to delete: ')
        dbdel = 'rm database/%s.db' % (dbdel)
        os.system(dbdel)

        c=input('Back to home (1): ')
        if c==1:
            os.system('clear')
            continue
        else:
            raise SystemExit

    elif c==9:

        print 'Goodbye!'
        raise SystemExit

    print '---------------------------------------------'
