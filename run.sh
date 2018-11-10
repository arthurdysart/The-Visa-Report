#!/bin/bash
#
# DESCRIPTION
# Runs The Visa Report with default input.
#
# TEMPLATE
# python3 <path-to-source-script> <path-to-input-csv> <path-to-output-1> <path-to-output-2>

python ./src/TheVisaReport.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt