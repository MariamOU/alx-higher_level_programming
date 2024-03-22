#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arguments = len(argv) - 1
    if num_arguments == 0:
        print("0 arguments.")

    else:
        print(f"{num_arguments} argument{'s' if num_arguments > 1 else ''}:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
