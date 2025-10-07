#!/usr/bin/python3
"""
    This Module Contains a function canUnlockAll
"""


def canUnlockAll(boxes):
    """
        This function is used to solve the Lockboxes

        Arguments:
            boxes: The boxes
    """
    key = set(boxes[0])
    #print(key)
    if len(key) == 0: return False
    i = 0
    while i < len(key):
        key.update(boxes[key[i]])
        #print(key)
        i += 1
    print(key) 
    if len(key) < len(boxes) - 1 or max(key) != len(boxes) - 1:
        return False
    if len(key) == len(boxes) - 1 and max(key) == len(boxes) - 1:
        return True
