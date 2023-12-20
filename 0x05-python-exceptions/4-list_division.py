#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            division = 0
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")

                division = my_list_1[i] / my_list_2[i]

                if my_list_2[i] == 0:
                    raise ZeroDivisionError("division by 0")

                new_list.append(division)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(division)
            except IndexError:
                print("out of range")
                new_list.append(division)
            except (TypeError, ValueError):
                print("wrong type")
                new_list.append(division)
        finally:
            pass

    return new_list
