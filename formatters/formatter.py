from formatters.stylish import stylish_format
from formatters.plain import plain_format
from formatters.json import json_format


def stringify_diff(diff: list, print_format: str) -> str:
    if print_format == 'plain':
        result = plain_format(diff)
    elif print_format == 'json':
        result = json_format(diff)
    elif print_format == 'stylish':
        result = stylish_format(diff)
    else:
        raise FileNotFoundError(f'Unknown format: {print_format}')
    return result
