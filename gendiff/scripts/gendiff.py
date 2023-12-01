#!/usr/bin/env python3
import argparse
from gendiff.engine import generate_diff
from tests.CONSTANTS import DESCRIPTION_GENDIFF


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION_GENDIFF)
    parser.add_argument("first_file",
                        help='Path to json or yml file')
    parser.add_argument("second_file",
                        help='Path to second file in same format')
    parser.add_argument("-f", "--format", default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output: stylish, plain or json')
    return parser.parse_args()


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
