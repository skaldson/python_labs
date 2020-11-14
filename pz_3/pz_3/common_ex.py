def correct_input() -> int:
    while True:
        try:
            return_val = int(input('Enter worker age : '))
        except ValueError:
            print('Value must be an integer')
            continue
        else:
            if return_val > 65 or return_val < 18:
                print('range : [18;65]')
                continue
            else:
                return return_val


class Worker:
    def __init__(self):
        self.age = correct_input() 
        self.name = input('Please enter worker name: ')
        self.__weight = 50
        self.__mood = 10
    
    def get_weight(self):
        return self.__weight

    def eat(self, how_much):
        if how_much > 10:
            self.age += 1
            self.__weight += how_much / 2
        else:
            self.__weight += how_much
    
    def walk(self):
        self.__mood += 1

    def dance(self):
        self.__mood += 2

    def work(self):
        if (self.__mood - 2) < 0:
            self.__mood = 0
        else:
            self.__mood -= 2

    def get_mood(self):
        return self.__mood

    def print_class(self):
        print(f'Name : {self.name}')
        print(f'Age: {self.age}')
        print(f'Weight: {self.get_weight()}')


wrk1 = Worker()
wrk1.eat(15)

for i in range(2):
    wrk1.dance()
    wrk1.walk()
wrk1.dance()

for i in range(9):
    wrk1.work()

print(f'Mood : {wrk1.get_mood()}')
wrk1.print_class()

