#!/usr/bin/python3
"""
    This Module contains a function that Returns a list of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
        This Function is used to generate a pascal triangle using a List
        
        Argument:
            - n: this is the integer used in generating the length of the pascal triangle.
        
        Return: This Function returns the Generated list of the Pascal Value based on the value of the n
                IF n <= 0. an empty list is returned.
    """
    new_list = []
    if n > 0:
        for i in range(n):
            new_list.append([1])
            for j in range(1, i):
                new_list[i].append(new_list[i-1][j-1] + new_list[i-1][j])
            if i > 0:
                new_list.append(1)

    return (new_list)