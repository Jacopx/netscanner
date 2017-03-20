import nmap
import datetime
import time
import os
import glob
from netf import *
# import netifaces

# Check if it's RUN with SUDO (root-permission)
if os.geteuid()!=0:
    print "You need root permissions to do this, zioooo!"
    raise SystemExit
# START THE MENU
c=0
while c!=9:
    c=menu(1)

    if c==1: # Simple Network Scan

        nm = nmap.PortScanner() # Calling NMAP function
        ip, mac, vend, name = scanner(nm) # Call function for scan
        printer(ip,mac,vend,name) # Calling print function
        c=input('Back to home (1): ')
        if c==1:
            os.system('clear')
            continue
        else:
            raise SystemExit

    elif c==2: # Net Database Comparison

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
            fa=open(netname, 'a', 0)
            menu(0)
        except: # If there is no database, create it!
            menu(0)
            print 'File opening failed!'
            print 'Creation of the new DB!'
            new=1
            f=open(netname, 'w+', 0)

        # Call scan function
        nm = nmap.PortScanner()
        ip, mac, vend, name = scanner(nm) # Function call for your network

        if new==1:
            typ=[]
            for i in range(len(mac)):
                typ.append('NEW')

            dbprinter(typ, ip, mac, vend, name)
            fprinter(f, typ, ip, mac, vend, name) # Calling print to file function

            c=input('Back to home (1): ')
            if c==1:
                os.system('clear')
                continue
            else:
                raise SystemExit
        else:

            typ = checkf(fr,ip,mac,vend) # Calling the checking batabase function

            dbprinter(typ, ip, mac, vend, name)
            m = input('Do you want to add this new host to the db (1): ')
            if m==1:
                fprinter(fa, ip, mac, vend, name, typ)

    elif c==3: # Showing Database

        os.system('clear')
        menu(0)
        db=glob.glob('database/*.db')

        for net in db:
            print '/%s' % (net)

        show = raw_input('Insert the Network Name to show: ')
        show = 'database/%s.db' % (show)

        # fr=open(show, 'r')
        # ip, mac, vend, name = show_file(fr)
        # printer(ip, mac, vend, name)

        try: # Try to open the database
            fr=open(show, 'r')
            ip, mac, vend, name = show_file(fr)
            printer(ip, mac, vend, name)
        except:
            print "Open failed!"

        c=input('Back to home (1): ')

        if c==1:
            os.system('clear')
            continue
        else:
            raise SystemExit

    elif c==4: # Edit Database

        print 'Function not already implemented, COOMING SOON!'

    elif c==5: # Clear Database

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

    elif c==9: # EXIT

        print 'Goodbye!'
        raise SystemExit

    print '---------------------------------------------'
