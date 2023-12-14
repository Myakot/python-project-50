from json import dumps
from gendiff.formatters.utils import get_key_info, get_children


def to_plain(diff: list) -> str:
    result = walk(diff, '')
    result = [item.strip() for item in result if item]
    return '\n'.join(result)


def walk(items: list, path: str) -> list:
    def process_item(item):
        name, type_, value = get_key_info(item)
        new_path = f'{path}{name}'
        match type_:
            case 'added':
                value_str = to_str(value)
                line = (f"Property '{new_path}' was added with value: "
                        f"{value_str}")
                return line
            case 'removed':
                line = f"Property '{new_path}' was removed"
                return line
            case 'nested':
                children = get_children(item)
                line = '\n'.join(walk(children, f'{new_path}.'))
                return line
            case 'changed':
                old_value, new_value = value
                old_value_str = to_str(old_value)
                new_value_str = to_str(new_value)
                line = f"Property '{new_path}' was updated." \
                       f" From {old_value_str} to {new_value_str}"
                return line
    result = list(map(process_item, items))
    return [line for line in result if line is not None]


def to_str(value) -> str:
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, bool) or value is None:
        value = dumps(value)
    elif isinstance(value, str):
        value = f"'{value.strip()}'"
    return str(value)
