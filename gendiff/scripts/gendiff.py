#!/usr/bin/env python3
from gendiff.generate_difference import generate_diff
from gendiff.cli import parse_args


def main():
    """
    Generate and print a diff between two files.

    This function takes no parameters.

    Returns:
        None
    """
    # Parse command line arguments
    args = parse_args()

    # Generate the diff using the specified format
    diff = generate_diff(args.first_file, args.second_file, args.format)

    # Print the diff
    print(diff)


if __name__ == '__main__':
    main()
