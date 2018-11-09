# -*- coding: utf-8 -*-
"""
The Visa Report v1.0 - Extract Module
Author: Arthur Dysart
Created on Fri Nov  9 10:19:18 2018

DESCRIPTION

Analyzes H1-B Visa data by most common "Occupation" and "State." Reports are
sorted by decreasing "Certified Visas" count and alphabetical "Occupation"
title.

This module contains functions for importing and verifying file system paths.
"""


## REQUIRED MODULES
import os


## MODULE DEFINITIONS
def get_args(sys_argv):
    """
    Sets command line arguments as file system paths from terminal.

    :param list[str] sys_argv: list of file system paths
    :return: list of verified file system paths
    :rtype: list[str]
    :raises IndexError: if incorrect number of file system paths    
    """
    n_args = len(sys_argv)

    if n_args == 4:
        in_path, occ_path, state_path = sys_argv[1:]

        # Verify input path points to existing file
        verify_in_path(in_path)
        # Verify output path does not point to existing file
        for pth in (occ_path, state_path):
            verify_out_path(pth)
        return in_path, occ_path, state_path
    else:
        raise IndexError("Incorrect argument specification. See "
                         "instructions in \"Read Me\" then run again.")

def verify_in_path(pth):
    """
    Verifies input file system path points to existing file.

    :param str pth: file system path to target file
    :return: True if target file exists
    :rtype: bool
    :raises FileNotFoundError: if target file not found
    """
    if not os.path.isfile(pth):
        raise FileNotFoundError("File not found in \"input\" directory.\n"
                                "Please confirm and run again.")
    else:
        return True

def verify_out_path(pth):
    """
    Verifies output file system path does not point to existing file.

    :param str pth: file system path to target file
    :return: True if target file does not exist
    :rtype: bool
    :raises FileExistsError: if target file already exists
    """
    if os.path.isfile(pth):
        raise FileExistsError("File already exists in \"output\" directory."
                              "\nPlease back up, remove, and run again.")
    else:
        return True


## MAIN MODULE
if __name__ == "__main__":
    pass


## END OF FILE