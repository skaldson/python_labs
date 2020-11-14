from correct_input import *


N = int()
K = int()
fell_skittles = 0

while True:
    print('Please enter N and K, respectively')
    temp = range_input(1, 100)

    if temp[1] > temp[0]:
        print('K must be <= N')
        continue
    else:
        N = temp[0]
        K = temp[1]
        break

skittles_line = ['I' for i in range(N)]

for i in range(K):
    if fell_skittles >= len(skittles_line):
        print('All skittles are fall')
        break
    
    print(f'Enter values [1, {N}]')
    temp = range_input(N, 1)
    segment_len = (max(temp) - min(temp)) + 1

    skittles_line[(min(temp) - 1):(max(temp))] = '.'*(segment_len )

    fell_skittles += (segment_len + 1)

for i in skittles_line:
    print(i, end='')
print()
