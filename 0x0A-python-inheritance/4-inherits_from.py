#!/usr/bin/python3
""" Module: 4-inherits_from """


def inherits_from(obj, a_class):
    """
        Return ture if objects is an instance of a class
        that inherited (directly or indirectly)

    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
