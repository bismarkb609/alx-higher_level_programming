#!/usr/bin/python3
""" Module : 2-is_same_class """


def is_same_class(obj, a_class):
    """
        Returns True if obj is an instance of a_class
        Args:
            obj : the object to check
            a_class : the class to match the obj to
    """

    if type(obj) == a_class:
        return True
    return False
