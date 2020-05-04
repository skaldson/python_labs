# interface for other classes: LocalNetwork, GlobalNetwork
from abc import ABC, abstractmethod


# class CalcNetwork
class CalcNetwork(ABC):
    def __init__(self, conn_type, area, speed, conn_amount):
        self.conn_type = conn_type
        self.area = area
        self.speed = speed
        self.conn_amount = conn_amount

    @abstractmethod
    def add_connection(self, new_conn):
        pass
   
    @abstractmethod
    def remove_connection(self):
        pass

    @abstractmethod
    def change_connection_type(self, new_type):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def increase_speed(self, how_many):
        pass

    @abstractmethod
    def decrease_speed(self, how_many):
        pass
    