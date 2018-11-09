# -*- coding: utf-8 -*-
"""
The Visa Report v1.0 - Main module
Author: Arthur Dysart
Created on Fri Nov  9 10:17:46 2018

DESCRIPTION

Analyzes H1-B Visa data by most common "Occupation" and "State." Reports are
sorted by decreasing "Certified Visas" count and alphabetical "Occupation"
title.
"""


## REQUIRED MODULES
import TheVisaReportExtract as vr1
import sys


## GLOBAL VARIABLES
# Hides traceback from terminal output
sys.tracebacklimit = None


## MAIN MODULE
if __name__ == "__main__":

    in_path, occu_path, state_path = vr1.get_args(sys.argv)


## END OF FILE