# Network Scanner

Useful network scanner for checking device linked to it written in Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. I'm working on the Python3 version!

### Prerequisites

The necessary software to run this script are Python and python-nmap:

```
brew install python
```
and
```
pip install python-nmap
```

## Dependencies

To run this script you will need this packages:
```
nmap datetime time os glob netifaces netaddr PrettyTable
```


### Installing

Simply clone this repository in your machine like this:

```
git clone https://github.com/Jacopx/netscanner.git
```

## Running the tests

This tools needs to be run with sudo (for nmap scan parameters). You need to change the interface of your network from the line 33:
```
add=netifaces.ifaddresses('en0')
```
The possible interface can be listed with (run it in Python):
```
>>> import netifaces
>>> netifaces.interfaces()
```

The Wi-Fi of a MacBook is normally 'en0'.

## Run the software

Start the Network Manager with:

```
sudo python netscan.py
```
You'll see a menu with the possibile function like this:
```
Network Scanner by Jacopx -- 21/12/2016 12:29
---------------------------------------------
1. Simple Network Scan
2. Net Database Comparison
3. Showing Database
4. Edit Database
5. Clear Database
9. EXIT
Choose:

```
You need to write the number of the function that you want to use:
* 1 --> Function to scan all your network simply showing the results in a table. From here you CAN'T save the result in a external file.
* 2 --> Function to scan all your network with database comparisons. The software will show all your database, if you add a name of a present db it will use it. If it's not already created it will build a new file.
* 3 --> Showing an already created database
* 4 --> NOT ALREADY IMPLEMENTED
* 5 --> Delete batabase
* 9 --> Bye Bye! ;)


## Built With

* [Python](http://pythoncentral.io) - The programming language
* [Python-NMAP](https://bitbucket.org/xael/python-nmap) - Python library use nmap port scanner

## Authors

* **Jacopo Nasi** - *Initial work* - [Jacopx](https://github.com/Jacopx)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Don't let anyones to break in your connection
