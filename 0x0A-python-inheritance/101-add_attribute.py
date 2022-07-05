#!/usr/bin/python3
""" Module 101-add_attributes """


def add_attribute(obj, att, value):
    """
    Args:
        obj : obj to add attr
        att : name of attr.
        value : value.
    Raises:
        TypeError: If attribute can't add.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
