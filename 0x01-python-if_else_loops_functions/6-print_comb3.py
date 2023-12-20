#!/usr/bin/python3
print("{:02d}".format(1), end='')
for i in range(2, 10):
    for j in range(i, 10):
        print(", {:02d}".format(i * 10 + j), end='')
print()
