#!/usr/bin/python3
""" Module : 6-load_from_json_file """

import json


def load_from_json_file(filename):
    """ Create an object from json file """
    with open(filename, encoding="utf-8") as myFile:
        return json.loads(myFile.read())
