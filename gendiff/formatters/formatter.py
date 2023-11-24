"""Formatter module - formatting the tree with the selected formatter"""

from gendiff.formatters import stylish, plain, json


def formatting(tree: dict, format_name="stylish") -> str:
    """Formatting the tree with the selected formatter."""
    formats = dict(stylish=stylish, plain=plain, json=json)
    if format_name in formats:
        return formats[format_name](tree)

    raise ValueError(f'Unknown format: {format_name}')
