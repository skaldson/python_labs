# module which describe peripheral classes: Computer, Printer, Fax
from random import choice, randint
import string

from network_devices import computer_processor, computer_type, printer_type, fax_type, fax_kind


# random string for peripheral names 
def random_name(string_length=6):
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(string_length))


# class Computer automatic initialization
class Computer():
    def __init__(self):
        self.name = 'computer_' + random_name()
        self.processor = choice(computer_processor)
        self.speed = 2**(randint(10, 12))
        self.memory = 2**(randint(8, 10))
        self.type = choice(computer_type)

    # print neccessary information
    def print_info(self):
        print(f'Name: {self.name}, type: {self.type}')


# class Printer automatic initialization
class Printer():
    def __init__(self):
        self.name = 'printer_' + random_name()
        self.printer_type = choice(printer_type)
        self.local = choice([True, False])
    
    # print neccessary information
    def print_info(self):
        print(f'Name: {self.name}, type: {self.printer_type}')


# class Fax automatic initialization
class Fax():
    def __init__(self):
        self.name = 'fax_' + random_name()
        self.fax_type = choice(fax_type)
        self.fax_kind = choice(fax_kind)
        self.local = choice([True, False])
    
    # print neccessary information
    def print_info(self):
        print(f'Name: {self.name}, type: {self.fax_type}')
