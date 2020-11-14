def input_number(low: int=1, up: int=9) -> int:
    while True: 
        try:
            num = input()
            if int(num) > up or int(num) < low:
                print(f'number : [{low}-{up}]')
                continue
            else:
                return int(num)
        except ValueError:
            print(f'Value must be an integer [{low}-{up}]')


file_name = 'peng'

try:
    with open(file_name) as peng_obj:
        peng_amount = input_number()

        peng_dict = dict()

        for i in peng_obj:
            peng_dict.setdefault(str(i[0:-1]), peng_amount)

        peng_list = list(peng_dict.keys())

        for i in peng_list:
            for j in range(peng_dict[i]):
                print(i, end=' ')
            print()
except FileNotFoundError:
    print(f'File {file_name} must be in current directory')
