#!/usr/bin/python3
"""
    This Module contains the UTF-8 Alx-interview Question solved
"""


def validUTF8(data):
    """
        This Method determines if a given data set represents a valid
        UTF-8 encoding

        Arguments:
            data: This is the data
    """
    for i in data:
        if i > (128):
            return False
    return True
