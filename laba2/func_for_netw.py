from math import ceil, floor
from random import choice, randint, getrandbits
from ipaddress import IPv4Address, IPv6Address

from network_devices import LanArea, WanArea
from network_devices import LanConnection as lan_conn
import peripheral


# print particular LAN items(devices)
def printLan_items(lan_conn):
    print('------LAN------')
    print('Deleting an item in LAN')
    for i in range(len(lan_conn)):
        print((i+1), end=': ')
        lan_conn[i].print_info()
        

# automatic add to LAN items
def addLan_connections(amount):
    if amount > 20:
        print('So big devices amount, now amount equal 20')
        amount = 20
    result = list()
    try:
        dev_amount = [ceil(abs(amount)/2), floor(abs(amount)/4)]
        for i in range(dev_amount[0]):
            result.append(peripheral.Computer())
        for i in range(dev_amount[-1]):
            result.append(peripheral.Printer())
            result.append(peripheral.Fax())
    except TypeError:
        print(f'Device amount is {type(amount)}')

    return result


# return random ip address for LAN 
def random_ip():
    bits = getrandbits(32)  
    addr = IPv4Address(bits) 
    addr_str = str(addr) 
        
    addr_str = addr.compressed 

    return (addr_str)
