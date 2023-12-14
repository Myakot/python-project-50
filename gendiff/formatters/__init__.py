from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import json_format


def stringify_diff(diff: list, print_format: str) -> str:
    match print_format:
        case 'plain':
            return to_plain(diff)
        case 'json':
            return json_format(diff)
        case 'stylish':
            return stylish_format(diff)
        case _:
            raise FileNotFoundError(f'Unknown format: {print_format}')


__all__ = ['stringify_diff']
