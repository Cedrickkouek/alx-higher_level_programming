#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ced = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                ced += 1
    except IndexError:
        pass
    finally:
        print()
        return ced
