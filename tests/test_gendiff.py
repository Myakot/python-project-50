import pytest


from gendiff.generate_difference import generate_diff, get_format_and_data
from gendiff.formatters import stringify_diff
from tests.utils import get_file_path
from tests.CONSTANTS import PATH_JSON_FLAT_RESULT


@pytest.mark.parametrize(
    'file1_path, file2_path, path_to_result',
    [
        ('file_1_flat.yml', 'file_2_flat.yaml', 'file_flat_result_yaml'),
        ('file_1_1.json', 'file_1_2.json', 'file_1_result_json'),
        ('file_2_1.json', 'file_2_2.json', 'file_2_result_json'),
    ],
    ids=['flat_yaml_file',  'json_file', 'json_2_file']
)
def test_generate_diff(file1_path, file2_path, path_to_result):
    expected_path = get_file_path(path_to_result)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_file_path(file1_path)
        test_path2 = get_file_path(file2_path)
        assert generate_diff(test_path1, test_path2) == result_data


@pytest.mark.parametrize(
    'file1_path, file2_path, print_format, path_to_result',
    [
        ('file_1_1.yml', 'file_1_2.yaml', 'stylish', 'file_1_result_json'),
        ('file_1_1.yml', 'file_1_2.yaml', 'json', 'file_1_format.json'),
        ('file_1_1.yml', 'file_1_2.yaml', 'plain', 'file_1_result_plain'),
        ('file_1_1.json', 'file_1_2.json', 'plain', 'file_1_result_plain'),
        ('file_2_1.json', 'file_2_2.json', 'plain', 'file_2_plain_result'),
        ('file_1_1.json', 'file_1_2.json', 'json', 'file_1_format.json'),
        ('file_2_1.json', 'file_2_2.json', 'json', 'file_2_format.json'),
    ],
    ids=['yml_yaml_stylish',  'yaml_to_json', 'yaml_to_plain', 'json_plain_file',
         'json_2_plain_file', 'json_format_file', 'json_2_format_file'])
def test_generate_diff_format(file1_path, file2_path, print_format, path_to_result):
    expected_path = get_file_path(path_to_result)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_file_path(file1_path)
        test_path2 = get_file_path(file2_path)
        assert generate_diff(test_path1, test_path2, print_format) == result_data


def test_open_exception():
    with pytest.raises(FileNotFoundError):
        get_format_and_data(PATH_JSON_FLAT_RESULT)


def test_stringify_exception():
    with pytest.raises(ValueError):
        stringify_diff('diff_data', 'unknown format')
