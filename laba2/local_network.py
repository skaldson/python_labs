# LocalNetwork class, descendant of CalcNetwork class
from random import randint, choice

from calc_network import CalcNetwork
from func_for_netw import addLan_connections, printLan_items, random_ip
from network_devices import LanConnection as lan_conn
from network_devices import LanArea
import is_correct


#function for add item in WAN
def addWan_connections(amount):
    if amount > 100:
        print('So big lan amount, now lan amount equal 100')
        amount = 100
    result = list()
    
    for i in range(amount):
        temp = LocalNetwork(choice(lan_conn.lanConn_list.value),
                            choice(LanArea.lanArea_list.value),
                            10**randint(2,4),
                            randint(6,17))
        result.append(temp)

    return result


# class LocalNetwork
class LocalNetwork(CalcNetwork):
    def __init__(self, conn_type=lan_conn.ethernet.value, area=LanArea.house.value, speed=100, conn_amount=5):
        super().__init__(conn_type, area, speed, conn_amount)
        self.conn_amount = addLan_connections(conn_amount)
        self.ip=random_ip()

    # add item in LAN
    def add_connection(self, new_conn):
        if len(self.conn_amount) < 20:
            if is_correct.is_lan_connection(new_conn):
                self.conn_amount.append(new_conn)
            else:
                print('Inncorrect lan connection')
        else:
            print('Sorry, devices limit reached')

    # remove item from LAN
    def remove_connection(self):
        printLan_items(self.conn_amount)
        choose = is_correct.input_number(r=len(self.conn_amount), message='which connection you want to delete ? ')
        self.conn_amount.pop(choose - 1)

    # change connection type in LAN
    def change_connection_type(self, new_type):
        if self.conn_type not in lan_conn.lanConn_list.value:
            print('Inncorrect lan connection')
        else:
            self.conn_type = new_type

    # inspect correct speed value in LAN
    def correct_speed_value(self):
        try:
            if self.speed < 0:
                print(f'Speed have negative value. Jetzt speed be {abs(self.speed)}')
                return abs(self.speed)
            else:
                return self.speed
        except TypeError:
            print('Speed type is str, so now program define random speed value')
            return 2**randint(7, 13)

    # increase speed value in LAN
    def increase_speed(self, how_many=50):
        try:
            if (self.speed + how_many) > 5000:
                print('Are you nuts ? It\'s impossible ')
            else:
                self.speed += how_many
        except TypeError:
            print(f'Increment have {type(how_many)} type')
    
    # decrease speed value in LAN
    def decrease_speed(self, how_many = 50):
        try:
            if (self.speed - how_many) < 10:
                print('It\'s impossible ')
            else:
                self.speed -= how_many
        except TypeError:
            print(f'Decrement have {type(how_many)} type')

    # print only info about devices which LAN contain
    def print_dev_info(self):
        for i in range(len(self.conn_amount)):
            print((i+1), end=': ')
            self.conn_amount[i].print_info()
    
    # print info about LAN
    def print_info(self):
        print('------LAN------')
        print(f'Connection Type: {self.conn_type}')
        print(f'Area: {self.area}')
        print(f'Speed: {self.correct_speed_value()}')
        print(f'Device amount: {len(self.conn_amount)}')
        print(f'LAN ip: {self.ip}')
        print()
