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
           Raises:
               TypeError: if size is not int
               ValueError: size less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
