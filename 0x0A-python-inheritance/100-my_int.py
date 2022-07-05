#!/usr/bin/python3
""" Module : 100-my_int """


class MyInt(int):
    """ == and != operators inverted """

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
