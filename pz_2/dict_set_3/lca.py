from functions import *


# test_1 roman_tribesmen
add_nodes(1, 2) # Alexei Peter_I
add_nodes(1, 3) # Anna Peter_I
add_nodes(1, 4) # Elizabeth Peter_I
add_nodes(2, 5) # Peter_II Alexei
add_nodes(3, 6) # Peter_III Anna
add_nodes(6, 7) # Paul_I Peter_III
add_nodes(7, 8) # Alexander_I Paul_I
add_nodes(7, 9) # Nicholaus_I Paul_I

counter_of_trying = correct_input(1, 5, 'Please, enter an amount of attempts : ')

print_tribesmen(roman_tribesmen)

for i in range(counter_of_trying):
    print_list_namen(test1)
    first = correct_input(1, 9)
    second = correct_input(1, 9)

    lowest_ancestor = test1[LCA(first, second) - 1]

    print(f'For {test1[first - 1]} and {test1[second - 1]} the lca is : {lowest_ancestor}')
    print()


# test_2 random_tribesmen
# for test_2 create a new tree, list_namen(test2) and list_tribesmen
# test_2 = ['ABVQKLSZG UNORTZGDM', 'ALOPAEPIX VYNYXUEQ', 
#             'DBPNBMCQ IDZTWEVFC', 'HHYVM NQXCK', 
#                 'IDZTWEVFC ABVQKLSZG', 'NQXCK VYNYXUEQ', 
#                     'SXIVZSOLAH HHYVM', 'UNORTZGDM ALOPAEPIX', 
#                         'UYPMDVMONF NQXCK']

