#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number == 0:
    print("Last digit of", number, "is", ld, end=" ")
    print("and is 0")
if number > 0:
    print("Last digit of", number, "is", ld, end=" ")
    if ld == 0:
        print("and is 0")
    elif ld > 5:
        print("and is greater than 5")
    else:
        print("and is less than 6 and not 0")
elif number < 0:
    if ld != 0:
        print("Last digit of", number, "is", -ld, end=" ")
        print("and is less than 6 and not 0")
