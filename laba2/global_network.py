#GlobalNetwork class, descendant of LocalNetwork class
from random import randint

from local_network import LocalNetwork, addWan_connections
from network_devices import WanConnection as wan_conn
from network_devices import WanArea
import is_correct


# class GlobalNetwork
class GlobalNetwork(LocalNetwork):
    def __init__(self, conn_type=wan_conn.cable.value, area=WanArea.city.value, speed=100, conn_amount=40):
        super().__init__(conn_type, area, speed, conn_amount)
        self.conn_amount = addWan_connections(conn_amount)
    
    # add item in WAN    
    def add_connection(self, new_conn):
        if len(self.conn_type) < 100:
            if type(new_conn) is LocalNetwork:
                self.conn_amount.append(new_conn)
            else:
                print('Inncorrect wan connection')
        else:
            print('Sorry, devices limit reached')
    
    # remove item from WAN
    def remove_connection(self):
        mesag = 'Deleting an item in WAN\n' + 'which connection you want to delete ? '
        choose = is_correct.input_number(r=len(self.conn_amount), message=mesag)
        self.conn_amount.pop(choose - 1)

    # change connection type in WAN
    def change_connection_type(self, new_type):
        if self.conn_type not in wan_conn.wanConn_list.value:
            print('Inncorrect wan connection')
        else:
            self.conn_type = new_type

    
    # inspect correct speed value in WAN
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

    # increase speed value in WAN
    def increase_speed(self, how_many=50):
        try:
            if (self.speed + how_many) > 1000:
                print('Are you nuts ? It\'s impossible ')
            else:
                self.speed += how_many
        except TypeError:
            print(f'Increment have {type(how_many)} type')

    # decrease speed value in WAN
    def decrease_speed(self, how_many = 50):
        try:
            if (self.speed - how_many) < 5:
                print('It\'s impossible ')
            else:
                self.speed -= how_many
        except TypeError:
            print(f'Decrement have {type(how_many)} type')

    # print info about WAN
    def print_info(self):
        print('------WAN------')
        print(f'Connection Type: {self.conn_type}')
        print(f'Area: {self.area}')
        print(f'Speed: {self.correct_speed_value()}')
        print(f'Device amount: {len(self.conn_amount)}')
        print()
