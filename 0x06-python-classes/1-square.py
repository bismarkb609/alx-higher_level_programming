#!/usr/bin/python3
""" Module Square """


class Square:
    """
       Square: defines a square class
       Attributes:
            size(no type/value identification): square size
        Method:
            __init__: init of size attribute for each instance
    """

    def __init__(self, size):
        """
           Initialize attributes
           Args:
               size(no type): square size
        """

        self.__size = size
