"""
Simple helper methods for processing CSV files
"""

from contextlib import contextmanager
import csv
import fileinput
import os
import logging

LOGGER = logging.getLogger("grocery")

class CSVUtils:
    def __init__(self, csv_filepath):
        self.filepath = csv_filepath

    # Returns parsed rows of CSV (excluding column names)
    def get_data_rows(self):
        data_rows = []
        try:
            with self.open_csv() as f:
                csvreader = csv.reader(f)
                parsed_csv = list(csvreader)
                data_rows = parsed_csv[1:]  # discard column names
        except FileNotFoundError:
            LOGGER.error("CSV file path doesn't exist")
            raise
        return data_rows

    # Open CSV in given mode (default is read mode)
    @contextmanager
    def open_csv(self, mode='r', newline=''):
        f = fileinput.input(files=(self.filepath), openhook=fileinput.hook_encoded("utf-8-sig"))
        try:
            yield f
        finally:
            f.close()
