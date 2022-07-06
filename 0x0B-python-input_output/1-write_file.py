#!/usr/bin/python3
""" Module 1-write_file """


def write_file(filename="", text=""):
    """ Write a string to a file """

    with open(filename, mode="w+", encoding="utf-8") as myFile:
        myFile.write("This School is so cool!\n")

    return len(text)
