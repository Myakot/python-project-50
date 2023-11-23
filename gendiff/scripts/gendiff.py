import argparse


parser = argparse.ArgumentParser()
parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()
print(args.echo)


'''
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
'''

