import math


class CircularSector:
    def __init__(self):
        self.__radius = 4
        self.__central_degree = 60

    def set_radius(self, value):
        try:
            self.__radius = int(value)
        except ValueError:
            print('Radius must be an integer')
            return False
        else:
            if self.__radius < 1 or self.__radius > 10000:
                print('Radius must be in [1;10000] range')
                print('radius = previous value')
                return False
    
    def set_central_degree(self, value):
        try:
            self.__central_degree = int(value)
        except ValueError:
            print('Central degree must be an integer')
            return False
        else:
            if self.__central_degree < 1 or self.__central_degree > 360:
                print('Central degree must be in [1;360] range')
                print('degree = previous value')
                return False

    def get_radius(self):
        return self.__radius

    def get_central_degree(self):
        return self.__central_degree

    def increase_parameters(self, how_much):
        if (self.__radius * how_much) > 360:  
            self.__central_degree = 360
            self.__radius *= how_much
            print('It\'s all now circle ', end='')
            print(f'central degree\'s equal {self.__central_degree} ')
            print(f'and __radius equal {self.__radius}')
        else:
            self.__central_degree *= how_much
            self.__radius *= how_much

    def decrease_parameters(self, how_much):
        if (self.__central_degree / how_much) < 1:
            self.__central_degree = 1
            self.__radius /= how_much
            print('It\'s all now circle ', end='')
            print(f'central degree\'s equal {self.__central_degree} ')
            print(f'and __radius equal {self.__radius}')
        else:
            self.__central_degree /= how_much
            self.__radius /= how_much

    def sector_area(self, pretty:bool = False):
        if pretty:
            area = str('%.2f'%(((self.__radius**2)*self.__central_degree)/360)) + '_pi'
        else:
            area = str('%.2f'%(((self.__radius**2)*self.__central_degree*math.pi)/360))

        return area

    def sector_lenght(self, pretty:bool = False):
        if pretty:
            lenght = str('%.2f'%((self.__radius*self.__central_degree)/180)) + '_pi'
        else:
            lenght = str('%.2f'%((self.__radius*self.__central_degree*math.pi)/180))

        return lenght

    def detect_diameter(self):
        return self.__radius * 2

    def detect_circle_lenght(self, pretty:bool = False):
        if pretty:
            return str('%.2f'%(self.detect_diameter())) + '_pi'
        else:
            return str('%.2f'%(self.detect_diameter()*math.pi))

    def print_sector_info(self):
        print(f'Sector lenght(pretty mode) : {self.sector_lenght(True)}')
        print(f'Sector Area : {self.sector_area()}')
        print(f'Circle lenght(pretty mode) : {self.detect_circle_lenght(True)}')
        print(f'Circle Diameter : {self.detect_diameter()}')


circle = CircularSector()

circle.set_radius(16)
circle.set_central_degree(90)

circle.decrease_parameters(2)
circle.increase_parameters(4)
circle.print_sector_info()
