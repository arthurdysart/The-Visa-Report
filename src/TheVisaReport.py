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
import TheVisaReportTransform as vr2
import TheVisaReportLoad as vr3
import sys


## GLOBAL VARIABLES
# Hides traceback from terminal output
sys.tracebacklimit = None


## MAIN MODULE
if __name__ == "__main__":

    in_path, occu_path, state_path = vr1.get_args(sys.argv)
    known_occus, known_states, n_cert = vr1.extract(in_path)

    occu_list = vr2.transform(known_occus, n_cert, top=None)
    vr3.load("occupations", occu_list, occu_path)

    state_list = vr2.transform(known_states, n_cert, top=None)
    vr3.load("states", state_list, state_path)


## END OF FILE