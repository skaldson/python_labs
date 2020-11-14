string = input('Please enter str : ')

l = string.split()

res = str()

for i in l:
    res += str(i) + ' '

print('Amount of words : ', res.count(' '))
