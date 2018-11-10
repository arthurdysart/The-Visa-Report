# -*- coding: utf-8 -*-
"""
The Visa Report v1.0 - Extract Module
Author: Arthur Dysart
Created on Fri Nov  9 10:19:18 2018

DESCRIPTION

Analyzes H1-B Visa data by most common "Occupation" and "State." Reports are
sorted by decreasing "Certified Visas" count and alphabetical "Occupation"
title.

This module contains functions for importing and verifying file system paths,
and extracting counts data for attributes "Occupation" and "State."
"""


## REQUIRED MODULES
import csv
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

def extract(in_path):
    """
    Analyzes input file for certified visa counts for attributes "Occupation"
    and "State," and determines the total number of certified visas.

    :param str in_path: file system path to target file
    :return: hash tables for all unique "Occupation" and "State" attributes
    :rtype: tup[dict[str: int], dict[str: int], int]
    """
    # Initialize total number of certifications
    n_cert = 0
    # Initialize dictionary with   key: unique occupation,
    #                            value: number of certified visas
    known_occus = {}
    known_states = {}

    with open(in_path, "r") as data_source:
        # Creates CSV iterator object to parse input file line-by-line
        read_csv = csv.DictReader(data_source,
                                  quotechar = "\"",
                                  delimiter = ";",
                                  quoting = csv.QUOTE_ALL,
                                  skipinitialspace = True)
        col_cert, col_occu, col_state = get_columns(read_csv.fieldnames)

        for row in read_csv:
            # Determines whether positive certification status
            if is_certified(row, col_cert):
                # Increments total number of certified H1B visas
                n_cert += 1
                for col_name in col_occu:
                    # Updates "known_occus" dictionary with given occupation
                    known_occus = update(row[col_name], known_occus)
                for col_name in col_state:
                    # Updates "known_states" dictionary with given state
                    known_states = update(row[col_name], known_states)
            else:
                continue
    return known_occus, known_states, n_cert

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

def update(key, known_attribs):
    """
    Adds row's occupation data to occupation dictionary of known certified 
    occupation counts.

    :param list[str] key: all values for row entry
    :param dict[str : int] known_attribs: hash tables for all unique attributes
    :return: dictionary with updated counts
    :rtype: dict[str : int]
    """
    if key != "":
        if key in known_attribs:
            known_attribs[key] += 1
        else:
            known_attribs[key] = 1
    return known_attribs

def is_certified(row, col_cert):
    """
    Evaluates whether given row entry has "certified" status.

    :param list[str] row: all values for row entry
    :param list[str] col_cert: all columns with status values
    :return: True if case number has "certified" status
    :rtype: bool
    """
    result = [True
              if row[col_name].upper() == "CERTIFIED"
              else False
              for col_name in col_cert]
    return any(result)

def get_columns(csv_column_names):
    """
    Sets command line arguments as file system paths from terminal.

    :param list[str] csv_column_names: all column names in target file
    :return: list of required column names
    :rtype: list[list[str]]
    """
    col_cert = [n for n in csv_column_names
                 if "STATUS" in n.upper()]

    col_occu = [n for n in csv_column_names
                if ("JOB" in n.upper() and
                    "TITLE" in n.upper())]

    col_state = [n for n in csv_column_names
                 if ("WORK" in n.upper() and
                     "STATE" in n.upper())]

    return col_cert, col_occu, col_state


## MAIN MODULE
if __name__ == "__main__":
    pass


## END OF FILE