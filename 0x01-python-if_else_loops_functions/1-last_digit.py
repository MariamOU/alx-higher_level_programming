#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Ld = number % 10
if Ld == 0:
    print("Last digit of {} is {} and is zero".format(number, Ld))
elif Ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, Ld))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, Ld)))
