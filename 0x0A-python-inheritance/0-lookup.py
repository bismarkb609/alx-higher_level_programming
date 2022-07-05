#!/usr/bin/python3
"""
    0-lookup module

"""


def lookup(self, obj):
    """
        Function returns all attributes and methods of an
        object.
        Args:
            obj: object whose attributes are to be listed

        Returns:
            list of attributes and methods of obj
    """

    return dir(obj)
