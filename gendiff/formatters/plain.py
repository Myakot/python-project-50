from json import dumps
from gendiff.formatters.get_data import get_name_type_value, get_children


def to_plain(diff: list) -> str:
    result = walk(diff, '')
    result = [item.strip() for item in result if item]
    return '\n'.join(result)


def walk(items: list, path: str) -> list:
    result = []
    for item in items:
        name, type_, value = get_name_type_value(item)
        new_path = f'{path}{name}'
        if type_ == 'added':
            value_str = to_str(value)
            line = f"Property '{new_path}' was added with value: {value_str}"
            result.append(line)
        elif type_ == 'removed':
            line = f"Property '{new_path}' was removed"
            result.append(line)
        elif type_ == 'nested':
            children = get_children(item)
            line = '\n'.join(walk(children, f'{new_path}.'))
            result.append(line)
        elif type_ == 'changed':
            old_value, new_value = value
            old_value_str = to_str(old_value)
            new_value_str = to_str(new_value)
            line = f"Property '{new_path}' was updated." \
                   f" From {old_value_str} to {new_value_str}"
            result.append(line)
    return result


def to_str(value) -> str:
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, bool) or value is None:
        value = dumps(value)
    elif isinstance(value, str):
        value = f"'{value.strip()}'"
    return str(value)
