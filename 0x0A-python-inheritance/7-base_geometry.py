#!/usr/bin/python3
""" Module 7-base_geometry """


class BaseGeometry(object):
    """ Denotes base geometry """

    def area(self):
        """ Not yet implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validate a parameter as int

            Args:
                name (str): name of parameter
                value (int): the parameter to validate
            Raises:
                TypeError: if value is not int
                ValueError: if value is <= 0

        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
