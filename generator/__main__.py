import argparse
from .grocery import Generator
from .utils import jsonutils
import logging
import sys

CSV_FILEPATH_HELP_MESSAGE = "Specify the filepath for the file to read CSV data from. To read from standard input"
JSON_FILEPATH_HELP_MESSAGE = "Specify the filepath for the file to output JSON data to. To write to standard output."
CONFIG_URL_HELP_MESSAGE = "Specify the URl which is to be configured in csv file"

def arg_parser():
    '''
     Returns the parsed arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_filepath', type=str, help=CSV_FILEPATH_HELP_MESSAGE)
    parser.add_argument('json_filepath', type=str, help=JSON_FILEPATH_HELP_MESSAGE)
    parser.add_argument("--url", type=str, help=CONFIG_URL_HELP_MESSAGE, required=False)
    return parser.parse_args()

def set_up_logger():
    # Create a custom logger
    logger = logging.getLogger("grocery")

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    date_fmt = "%a %d %b %Y %H:%M:%S"
    c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s - %(message)s', date_fmt)
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    return logger

def main():
    try:
        logger = set_up_logger()
        args = arg_parser()
        logger.info("Converstion from csv to json started")
        if args.url:
            generator = Generator(args.csv_filepath, args.url)
        else:
            generator = Generator(args.csv_filepath)
        json_struct = generator.convert()
        jsonutils.output_json(json_struct.as_dict(), args.json_filepath)
        logger.info("Nested json file created at specidfed output file")
    except Exception as err:
        raise SystemExit(1)
    