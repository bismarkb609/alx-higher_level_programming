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

        @property
        def size(self, value):
            """
            getter of size
            Return:
                Size of square
            """

        @size.setter
        def size(self, value):
            """
            setter of size
            Args:
                value (int): size of the square side
            Raises:
                TypeError: if the size is not int
                ValueError: size less than 0
            Returns:
                None
            """

            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """
            Compute area of the square
            Return:
                Area of square
            """
            return self.__size ** 2

        def my_print(self):
            """ Print a square with # """

            if self.__size == 0:
                print()
            else:
                for x in range(self.__size):
                    print("#" * self.__size)
