# -*- coding: utf-8 -*-
"""
The Visa Report v1.0 - Transform Module
Author: Arthur Dysart
Created on Fri Nov  9 10:58:39 2018

DESCRIPTION

Analyzes H1-B Visa data by most common "Occupation" and "State." Reports are
sorted by decreasing "Certified Visas" count and alphabetical "Occupation"
title.

This module contains functions for extracting counts data by attributes
"Occupation" and "State."
"""


## MODULE DEFINITIONS
def transform(attribute, n_cert, top=None):
    """
    Creates list of specified attribute according to certified visa count, then
    updates with percentage of certified applications.

    :param dict[str: int] attribute: hash table of all unique attribute values
    :param int n_cert: number of certified applications
    :param int top: total number of analyzed attribute values to load
    :return: list 
    :rtype: list[str]
    :raises IndexError: if attributes contains no entries
    :raises IndexError: if specified top number is out of bounds
    """
    # Verify attribute contains at least one entry
    if not attribute:
        raise IndexError("Extracted data contains no entries. Check "
                         "contents of input file then run again.")

    # Verify top number is correct type and greater than 0
    if isinstance(top, int):
        if (top < 1 or
            top > len(attribute)):
            raise IndexError("Specified top number is out of bounds. See "
                             "instructions in \"Read Me\" then run again.")

    attrib_list = sorted(attribute.items(),
                         key=sort_order)[:top]

    attrib_list = [cast(name, count, n_cert)
                   for (name, count)
                   in attrib_list]

    return attrib_list

def sort_order(item):
    """
    Sorts attributes (e.g., occupation, state) by (1) decreasing count for 
    number of certified applications, then (2) alphabetic order of name.

    :param tup[str, int] item: attribute name and count
    :return: modified attribute name and count
    :rtype: tup[int, str]
    """
    return -1 * item[1], item[0]

def cast(name, count, n_cert):
    """
    Returns formatted string with relevant values.

    :param str name: attribute name
    :param int count: attribute count
    :param int n_cert: total number of certified applications
    :return: formatting string for attribute entry
    :rtype: str
    """
    # Calculates percentage of certified visas for specified attribute
    percent = round(count * 100/ n_cert, 1)
    return ";".join([name,
                     str(count),
                     str(percent) + "%"])


## MAIN MODULE
if __name__ == "__main__":
    pass


## END OF FILE