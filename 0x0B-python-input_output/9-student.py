#!/usr/bin/python3
""" Module : 9-student """


class Student(object):
    """
        A student Class

    """
    def __init__(self, first_name, last_name, age):
        """ Initialize Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrieve a dictionary representation of a Student
        """
        return self.__dict__
