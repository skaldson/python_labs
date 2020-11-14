def range_input(l: int, r: int):
    temp_list = [l ,r]

    while True:
        try:
            numbers_list = input().split()[0:2]
            result_list = [int(numbers_list[0]), int(numbers_list[1])]
        except ValueError:
            print(f'Value must be an interger [{min(temp_list)}, {max(temp_list)}]')
            continue
        except IndexError:
            print('Enter should contain two values')
            continue

        min_in_range = min(result_list) >= min(temp_list) and min(result_list) <= max(temp_list)
        max_in_range = max(result_list) >= min(temp_list) and max(result_list) <= max(temp_list)

        if min_in_range and max_in_range:
            return result_list
        else:
            print(f'Out of range [{min(temp_list)}, {max(temp_list)}]')
            continue