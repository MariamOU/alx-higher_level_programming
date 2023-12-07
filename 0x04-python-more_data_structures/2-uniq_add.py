#!/usr/bin/python3
def uniq_add(my_list=[]):
    U_integers = set()

    for number in my_list:
        U_integers.add(number)

    add_numbers = sum(U_integers)
    return add_numbers
