def gcd(a, b):
    if int(b) == 0:
        return int(a)
    else:
        return gcd(int(b), int(a % b))

state = False

while not state:
    try:
        a = int(input())
        b = int(input())
        state = True
    except ValueError:
        print('Value must be an integer')
        state = False

if (a) >= (b):
    print(f'gcd({a}, {b}): {gcd(a,b)}')
else:
    print(f'gcd({b}, {a}): {gcd(b, a)}')
