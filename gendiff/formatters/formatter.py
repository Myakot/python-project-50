from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


def stringify_diff(diff: list, print_format: str) -> str:
    if print_format == 'plain':
        return plain_format(diff)
    elif print_format == 'json':
        return json_format(diff)
    elif print_format == 'stylish':
        return stylish_format(diff)
    else:
        raise FileNotFoundError(f'Unknown format: {print_format}')
