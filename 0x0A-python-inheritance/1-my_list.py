#!/usr/bin/python3
"""
    Module: 1-my_list

"""


class MyList(list):
    """
        class MyList
        methods:
            print_sorted: prints a sorted list
    """

    def print_sorted(self):
        """ Print the list in ascending order  """

        print(sorted(self))
