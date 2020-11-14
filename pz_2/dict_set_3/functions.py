test1 = ['Peter_I', 'Alexei', 'Anna', 'Elizabeth', 
                        'Peter_II', 'Peter_III', 'Paul_I', 'Alexander_I', 'Nicholause_I']

roman_tribesmen = ['Alexei Peter_I', 'Anna Peter_I', 'Elizabeth Peter_I',
                            'Peter_II Alexei', 'Peter_III Anna', 'Paul_I Peter_III',
                                    'Alexander_I Paul_I', 'Nicholause_I Paul_I']

MAXN = 100001

tree = [[] for i in range(MAXN)]
path = [[[] for i in range(MAXN)] for j in range(3)]


def dfs(cur: int, prev: int, pathNumber: int, ptr: int, node: int, flag: bool):
    for i in range(len(tree[cur])):
        if (tree[cur][i] != prev) and not flag:
            path[pathNumber][ptr] = tree[cur][i]
            if tree[cur][i] == node:
                flag = True

                path[pathNumber][ptr + 1] = -1
                return

            dfs(tree[cur][i], cur, pathNumber, ptr+1, node, flag)

def LCA(a: int, b: int):
    if a == b:
        return a

    path[1][0] = path[2][0] = 1

    flag = False
    dfs(1, 0, 1, 1, a, flag)

    flag = False
    dfs(1, 0, 2, 1, b, flag)

    i = 0
    while path[1][i] == path[2][i]:
        i += 1

    return path[1][i - 1]

def add_nodes(a: int, b: int):
    tree[a].append(b)
    tree[b].append(a)


def correct_input(l: int=1, r: int=9, inv_mes: str='Please enter a number : '):
    number = int()
    while True:
        try:
            number = int(input(inv_mes))
        except ValueError:
            print('Value must be an integer : ')
            continue
        else:
            if number < l or number > r:
                print(f'Value must be in [{l}, {r}] range')
            else:
                return number


def print_tribesmen(list_namen):
    for i in list_namen:
        print(i)
    print()


def print_list_namen(namen: list):
    for i in test1:
        if (test1.index(i) + 1) % 4 == 0:
            print(i, '->', test1.index(i) + 1)
        else:   
            print(i, '->', test1.index(i) + 1, end=' ')
    print()
