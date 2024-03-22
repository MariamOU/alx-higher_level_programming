#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_arguments = len(argv) - 1
    if number_arguments == 0:
        print("0 arguments.")
        print(".")
    else:
        print(f"{number_arguments} argument{'s' if number_arguments > 1 else ''}:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
