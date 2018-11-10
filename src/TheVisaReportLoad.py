# -*- coding: utf-8 -*-
"""
The Visa Report v1.0 - Load module
Author: Arthur Dysart
Created on Sat Nov 10 13:37:19 2018

DESCRIPTION

Analyzes H1-B Visa data by most common "Occupation" and "State." Reports are
sorted by decreasing "Certified Visas" count and alphabetical "Occupation"
title.

This module contains functions for loading transformed data into output file.
"""


## MODULE DEFINITIONS
def load(attrib_name, attrib_list, out_path):
    """
    Exports formatted entries for top attributes to specified output file.

    :param str attrib_name: attribute name
    :param list[str] attrib_list: formatted entries for top attributes
    :return: None
    :rtype: None
    """
    header = (f"TOP_{attrib_name.upper()};"
              "NUMBER_CERTIFIED_APPLICATIONS;"
              "PERCENTAGE\n")

    with open(out_path, 'w') as target_file:
        target_file.write(header)
        # Writes all intermediate entries with trailing new line character
        for entry in attrib_list[:-1]:
            target_file.write(entry + "\n")
        # Writes last entry without new line character
        target_file.write(attrib_list[-1])
    return None


## MAIN MODULE
if __name__ == "__main__":
    pass


## END OF FILE