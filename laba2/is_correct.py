# check correct range input and correct lan connection type
from peripheral import Computer, Printer, Fax


# check new lan connection
def is_lan_connection(my_type):
    types = [type(Computer()), type(Fax()), type(Printer())]
    return (True if type(my_type) in types else False)


# check correct input
def input_number(r, message, l: int = 1):
    while True:
        try:
            num = input(str(message)+f'[{l}-{r}] : ')
            if int(num) > r or int(num) < l:
                print(f'number : [{l}-{r}]')
                continue
            else:
                return int(num)
        except ValueError:
            print(f'Value must be an integer [{l}-{r}]')
