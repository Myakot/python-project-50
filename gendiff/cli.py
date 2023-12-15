import argparse
from CONSTANTS import DESCRIPTION_GENDIFF


def parse_args():
    """ Separate CLI module that is responsible for working with
    the console the function returns a tuple (file1, file2, formatter) """

    parser = argparse.ArgumentParser(description=DESCRIPTION_GENDIFF)
    parser.add_argument("first_file",
                        help='Path to json or yml file')
    parser.add_argument("second_file",
                        help='Path to second file in same format')
    parser.add_argument("-f", "--format", default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output: stylish, plain or json')
    return parser.parse_args()
