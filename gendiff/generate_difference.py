from gendiff.diff import create_diff
from gendiff.parser import parse
from gendiff.formatter import stringify_diff


def open_(path: str) -> tuple[str, str]:
    with open(path, 'r') as stream:
        text = stream.read()
    if path.endswith('.json'):
        data_format = 'json'
    elif path.endswith('.yml') or path.endswith('.yaml'):
        data_format = 'yml'
    else:
        raise FileNotFoundError('Unknown file format')
    return text, data_format


def generate_diff(file1_path: str, file2_path: str, format='stylish') -> str:
    ''' Compares two configuration files and return string with difference
    :param file1_path: Path to the first file
    :param file2_path: Path to the second file
    :param format: Output format: 'stylish' - default, 'plain' or 'json'
    :return: str
    '''
    data_1 = parse(*open_(file1_path))
    data_2 = parse(*open_(file2_path))
    diff = create_diff(data_1, data_2)
    result = stringify_diff(diff, format)
    return result
