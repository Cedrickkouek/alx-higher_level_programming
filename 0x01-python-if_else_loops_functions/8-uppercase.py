#!/usr/bin/python3

def uppercase(anystring):
    """Prints an uppercase String"""
    for c in anystring:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
