#!/usr/bin/python3
"""
  1-my_list module
  class Mylist that inherits from list
  Public instance method : def print_sorted(self)
"""


class MyList(list):
    """ Contain a function with sorted list """

    def print_sorted(self):
        """ Print the list in ascending order  """
        print(sorted(self))
