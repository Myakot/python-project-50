from json import dumps
from gendiff.formatters.utils import get_key_info, get_children
from gendiff.constants import TAB_STEP


def stylish_format(diff: list) -> str:
    return '{\n' + dive(diff, 0) + '\n}'


def dive(items: list, depth: int) -> str:
    result = []
    for item in items:
        name, type_, value = get_key_info(item)
        if type_ == 'nested':
            children = get_children(item)
            lines = make_line(depth, ' ', name, children=children)
        elif type_ == 'added' or type_ == 'removed':
            sign = '+' if type_ == 'added' else '-'
            lines = make_line(depth, sign, name, value)
        elif type_ == 'changed':
            value_1, value_2 = value
            lines_1 = make_line(depth, '-', name, value_1)
            lines_2 = make_line(depth, '+', name, value_2)
            lines = f'{lines_1}\n{lines_2}'
        elif type_ == 'unchanged':
            lines = make_line(depth, ' ', name, value)
        else:
            raise TypeError('Type not found: {}'.format(type_))
        result.append(lines)
    return '\n'.join(result)


def make_line(depth: int, sign: str, name: str,
              value=None, children=None) -> str:
    begin = f'{depth * TAB_STEP}  {sign} {name}: '
    end = f"\n{depth * TAB_STEP}    " + '}'
    if children:
        dive_result = dive(children, depth + 1)
        result = begin + '{\n' + dive_result + end
    elif isinstance(value, dict):
        lines = []
        value_sorted = dict(sorted(value.items()))
        for name, value in value_sorted.items():
            lines.append(make_line(depth + 1, ' ', name, value))
        result = begin + '{\n' + '\n'.join(lines) + end
    elif isinstance(value, bool) or value is None:
        result = begin + dumps(value)
    else:
        result = begin + str(value).strip()
    return result
