# Grocery
Converst csv to nested JSON

## Table of Contents
<!--ts-->
   + [Getting Started](#getting-started)
      + [Installation](#installation)
      + [Tools Used](#Tools-Used)
      + [Language](#Language)
      + [Expectation and output](#Expectation-and-output)
      + [Usage: Command Line](#usage-command-line)
   + [Development](#development)
      + [Running tests](#running-tests)
<!--te-->

# Getting Started
 Available as [command line tool](#usage-command-line).
 
# Tools Used
1.visual studios
2.git bash

# Language
1.python

# Expectation and output
 Data csv provided with different level of parent and child grocery data and each level will mandatoryly contain Name,ID and URl, then application will convert the CSV data into nested json structure. URL is also configurable.
 
To Update the URL use --url optional argument and provide the part which is to be update if groceries.abc.com is to be replace with groceries.xyz.com
provide "generator cvs_filepath json_filepath --url groceries.xyz.com"
 

# Installation
 1.Clone the repo
 2.Run pip install grocery-0.0.1-py3-none-any.wheel
 
# Usage Command line
 ```shell
 generator -h
usage: generator [-h] [--url URL] csv_filepath json_filepath

positional arguments:
  csv_filepath   Specify the filepath for the file to read CSV data from. To read from standard input
  json_filepath  Specify the filepath for the file to output JSON data to. To write to standard output.

optional arguments:
  -h, --help     show this help message and exit
  --url URL      Specify the URl which is to be configured in csv file
 ```
 
### CSV		

| .    | Level 1 - N | Level1-ID |Level 1 - URL|Level2-Nmae|Level2-ID| Level 2 - URL| 
|------|-------------|-----------|-------------|-----------|---------|--------------| 
|URL1  | THE BEST    | 178974    | URL2        |   FRESH   | 178969  |  URL3        |

URL1 : https://groceries.abc.com/browse
URL2:  https://groceries.abc.com/browse/178974
URL3:  https://groceries.abc.com/browse/178974/178969
### Generated JSON
```
{
    "name": "grocery",
    "children": [
        {
            "name": "THE BEST",
            "ID": "178974",
            "url": "https://groceries.abc.com/browse/178974",
            "children": [
                {
                    "name": "FRESH",
                    "ID": "178969",
                    "url": "https://groceries.abc.com/browse/178974/178969",
                    "children": []
                }
            ]
        }
    ]
}
```

## Development
### Running tests
From the root directory of this repository, run `python3 -m unittest` to execute the entire test suite.
