#!/usr/bin/python3
"""
    0-lookup module
    Output available attributes and method of an object

"""


def lookup(self, obj):
    """
        Function returns all attributes and methods of an
        object.
    """

    return [method_name for method_name in dir(obj)]
