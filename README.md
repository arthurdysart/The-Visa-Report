The Visa Report: ETL processing of historal H-1B data

# Navigation
1. [QUICK START](README.md#Quick-start-guide)
2. [MECHANISMS](README.md#Mechanisms)
3. [REQUIREMENTS](README.md#Requirements)
4. [CREDITS](README.md#Credits)

The Visa Report (TVR) performs extract-transform-load (ETL) tasks to analyze H-1B visa data. TVR is compatible with comma-separated value data from the United States Department of Labor Office of Foreign Labor Certification. For each occupation and workplace state, TVR reports ***total number of certified visas*** and ***percentage of certified visas***. Analysis reports are organized by occupation or workplace state in sequence of ***decreasing total number of certified visas*** and ***alphanumeric occupation or workplace state***.


# Quick start guide

TVR is built on CPython 3.6 and requires the `csv`, `os`, and `sys` modules. TVR can also be executed via the Apache Spark distributed computation engine.

## Installation and setup
Download Github repository. Install [CPython](https://www.python.org/downloads) version 3.6 and [Git Bash](https://git-scm.com/downloads); ensure both are available on the operating system path. Put the input data file in the `input/` directory. Note TVR only analyzes comma-delimited plaintext data which follow the [formatting guidelines of the Office of Foreign Labor Certification](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).

Analysis is executed using shell script or command line interface. Alternatively, TVR can be executed using [Apache Spark](https://spark.apache.org/) via [Jupyter iPython Notebook](https://hub.docker.com/r/jupyter/pyspark-notebook/) (preconfigured suite available as [Docker](https://docs.docker.com/engine/docker-overview/) image).


## Apache Spark
[Apache Spark](https://spark.apache.org/) is an open-source distributed computation engine. The preconfigured [Jupyter-Spark Docker image](https://hub.docker.com/r/jupyter/pyspark-notebook/) is recommended. Detailed instructions for Docker installation are [available here.](https://docs.docker.com/install/)

From the root project directory, the Docker image is downloaded and executed using the following command:

```
docker run -p 8888:8888 -p 8080:8080 -p 4040:4040 -v $(pwd):/home/jovyan/work jupyter/all-spark-notebook
```

- **`docker run`** indicates execution of target Docker image. If image unavailable, the most recent image is pulled from the Docker repository.
- **`-p 8888:8888`** enables the Jupyter Notebook UI on port 8888 of the local host node.
- **`-p 8080:8080`** enables the Spark Task Overview UI on port 8080 of the local host node.
- **`-p 4040:4040`** enables the Spark Cluster Overview UI on port 4040 of the local host node.
- **`-v $(pwd):/home/jovyan/work`** maps the current working directory to the Jupyter Notebook default directory.
- **`jupyter/all-spark-notebook`** identifies the target Docker image preconfigured with Jupyter iPython Notebook and Apache Spark.

The TVR analysis script is available as a Jupyter iPython Notebook in the `src_spark/` directory. Ensure the docker container is executed from the root project directory to access project subdirectories (viz., input and output directories and contents).

To terminate the running Docker container, execute the following commands:

```
docker container ls
docker stop [container ID]
```


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


# Mechanisms

TVR manages, processes, and displays data for all certified H-1B visa applications in its knowledge base using Python’s built-in data analysis functions. Compatible input data is organized by attributes of occupation and state, and is aggregated by (1) the total number of certified applications and (2) the percentage of associated certified H-1B visas relative to all certified applications. For each unique attribute, ***number of certified visas*** and ***percentage of certified visas for attribute*** are reported in order of ***decreasing number of certified visas*** and ***alphanumeric order***.

Before extracting data, TVR validates specified import and export paths: if incorrect, `file not found` and `file already exists` errors are respectively raised and script execution is terminated.

Data is imported using Python’s built-in **`open()`** function and **`with… as`** statement, and parsed line-by-line according to semi-colon delimiters using the `csv` module. Strings containing non-delimiting semi-colon characters are natively-handled by the `csv` module.

Due to schema variability, relevant attributes (viz., visa status, SOC occupation name, and workplace state) have different column headers for each year of reported H-1B visa data. Among over 35 various attributes, the column corresponding to each attribute is identified using the **`get_columns()`** function according to the following keywords:

| Attribute             | Identification Criteria           |
|-----------------------|-----------------------------------|
| Case status           | "STATUS" in column name           |
| Occupation name (SOC) | "SOC" and "NAME" in column name   |
| Workplace state       | "WORK" and "STATE" in column name |

TVR successfully identifies relevant attribute columns for H-1B visa historical data between 2014 - 2016, and is expected to be forward-compatible with future data.

Extracted data is stored in a dictionary, Python's implementation of the hash map data structure. For occupation-focused analysis, the hash key is unique occupation name; for state-focused analysis, the hash key is unique state abbreviation. As identified by the **`is_certified()`** function, certified visas are counted in the hash value of either the **`known_occus`** or **`known_states`** dictionaries: counters are initialized or incremented with one unit count for corresponding SOC occupation name or workplace state abbreviation, respectively.

After parsing, key-value pairs in each attribute dictionary (i.e., SOC occupation name or workplace state abbreviation) are sorted in order of: (1) decreasing total number of certified visas and, in case of identical counts, (2) alphanumeric order of attribute name. The first or "top" entries for each attribute are determined by the **`top`** keyword argument of the **`transform()`** function, then formatted as semi-colon delimited string for export.

Data export is performed using Python’s built-in **`write()`** function. In correctly sorted order, transformed and formatted data for each attribute are written to corresponding output text files. After writing all entries, the file is automatically closed and the script run is complete.


# Requirements

TVR requires CPython 3.6 and the `csv`, `os`, and `sys` modules. The script can be executed via Bash shell script or CPython command line interface.

TVR consists of four modules located in the `src/` directory. The `src/TheVisaReport.Py` module is the main script that controls data extraction (i.e., import), transformation (analysis and sorting), and external loading (export). The `src/TheVisaReportExtract.Py` module contains all functions related to validation of IO paths in the local file system, and extraction of H-1B visa data from the source file. The `src/TheVisaReportTransform.Py` module contains all functions related to sorting extracted data (by decreasing order of number of certified visas, then alphanumeric order of attribute name) and formatting data for external export. The `src/TheVisaReportLoad.Py` module contains all functions related to exporting transformed data to specified output paths.


# Credits

This project was created by Arthur Dysart as part of the 2018 [Insight Data Engineering Fellowship](https://www.insightdataengineering.com/). Scripts developed using Spyder IDE.

During development, sample data was obtained from the [United States Department of Labor Office of Foreign Labor Certification](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). The pre-cleaned data for each H-1B visa application includes over 35 columnar attributes including case metadata, milestone dates, employer information, occupation details, solicitation details, and applicant information.