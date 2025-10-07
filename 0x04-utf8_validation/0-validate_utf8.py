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
    def number_of_bytes(byte):
        """
        """
        if (byte >> 7) == 0b0:
            return 1
        elif (byte >> 5) == 0b110:
            return 2
        elif (byte >> 4) == 0b1110:
            return 3
        elif (byte >> 3) == 0b11110:
            return 4
        return 0

    expected_byte = 0
    for byte in data:
        if expected_byte == 0:
            expected_byte = number_of_bytes(byte)
            if expected_byte == 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_byte -= 1 
    return expected_byte == 0
