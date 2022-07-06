#!/usr/bin/python3
""" Module : 5-save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """
        Write an object to a text file; JSON representation
        Args:
            my_obj: object to write
            filename: name of the file

    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
