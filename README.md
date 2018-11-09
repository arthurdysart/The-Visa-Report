The Visa Report: ETL processing of historal H-1B data

Navigation
1. [QUICK START](README.md#Quick-start-guide)
2. [REQUIREMENTS](README.md#Requirements)
3. [CREDITS](README.md#Credits)

The Visa Report (TVR) performs extract-transform-load (ETL) tasks to analyze H-1B Visa data. TVR is compatible with is comma-separated value data from the United States Department of Labor Office of Foreign Labor Certification. For each occupation and workplace state, TVR reports ***total number of certified visas*** and ***percentage of certified visas***. Analysis reports are organized by occupation or workplace state in sequence of ***decreasing total number of certified visas*** and ***alphanumeric occupation or workplace state***.


# Quick start guide

TVR is built on Python 3.6 and requires the `csv`, `os`, and `sys` modules.

## Installation and setup
Download Github repository. Install [CPython](https://www.python.org/downloads) version 3.6 and [Git Bash](https://git-scm.com/downloads); ensure both are available on the operating system path. Put the input data file in the `input/` directory. Note TVR only analyzes comma-delimited plaintext data which follow the [formatting guidelines of the Office of Foreign Labor Certification](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).

Analysis is executed using shell script or command line interface.


## Shell script
Execute `run.sh` in the repository root directory to extract, transform, and load data. The shell script can also be executed in command line while in the repository root directory:

```
bash run.sh
```

- **`bash`** indicates script execution using the bash shell command.
- **`run.sh`** indicates the preconfigured shell script for default execution.

Ensure source file exists in `input/` directory, and target files do not exist in `output/` directory. The preconfigured `run.sh` script analyzes sample data from `input/H1B_FY_2014.txt` source file and exports analysis results to `output/top_10_occupations.txt` and `output/top_10_states.txt` target files.

To analyze custom data, update import and export paths in `run.sh` using a text editor. Ensure data is of comma-separated value format and follows [formatting guidelines of the Office of Foreign Labor Certification](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).


## Command line interface
Execute the following command:

```
python3    [main path]    [import path]    [occupations export path]    [state export path]
```

- **`python3`** indicates script execution using CPython 3 interpreter.
- **`main path`** indicates main script location. From the home directory, the main path is `./src/TheVisaReport.Py`.
- **`import path`** indicates input file location. Using sample data, the import path is `./input/H1B_FY_2014.csv`.
- **`occupations export path`** indicates output file location for occupation-focused analysis. Using sample data, the export path is `./output/top_10_occupations.txt`.
- **`state export path`** indicates output file location for state-focused analysis. Using sample data, the export path is `./output/top_10_states.txt`.


# Requirements

TVR requires CPython 3.6 and the `cv`, `os`, and `sys` modules. The script can be executed via Bash shell script or CPython command line interface.

TVR consists of four modules located in the `src/` directory. The `src/TheVisaReport.Py` module is the main script that controls data extraction (i.e., import), transformation (analysis and sorting), and external loading (export). The `src/TheVisaReportExtract.Py` module contains all functions related to validation of import and export paths in the local file system.


# Credits

This project was created by Arthur Dysart as part of the 2018 [Insight Data Engineering Fellowship](https://www.insightdataengineering.com/). Scripts developed using Spyder IDE.

During development, sample data was obtained from the [United States Department of Labor Office of Foreign Labor Certification](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). The pre-cleaned data for each H-1B visa application includes over 35 columnar attributes including case metadata, milestone dates, employer information, occupation details, solicitation details, and applicant information.