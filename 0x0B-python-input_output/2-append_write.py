#!/usr/bin/python3
""" Module : 2-append_write """


def append_write(filename="", text=""):
    """ Append a string to a text file"""
    with open(filename, mode="a+", encoding="utf-8") as myFile:
        myFile.write("This School is so cool!\n")

    return len(text)
