#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ced = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                ced += 1
            except IndexError:
                continue
    finally:
        print()
        return ced
