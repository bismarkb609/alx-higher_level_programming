#!/usr/bin/python3
""" Moduel 2-rectagle
Defines a Rectangle class.
"""


class Rectangle:
    """Represent class defined by shape
    -Instantiation with size
    Attributes:
         width (int): width of rectangle
         height (int): height of rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width of rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the width """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of a rectangle instance
        Returns:
            Area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Compute the perimeter of a rectangle instance
        Returns:
            Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
