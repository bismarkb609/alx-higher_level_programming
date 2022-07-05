#!/usr/bin/python3
""" My List class """


class MyList(list):
    """ Contain a function with sorted list """

    def print_sorted(self):
        """ Sort a list """

        print(sorted(self))
