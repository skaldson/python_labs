m = 6
n = 5

array = [[(j%3 + i)%3 for i in range(n + 1)] for j in range(m, 1, -1)]

for i in array:
    for j in i:
        print(j, end=' ')
    print()
