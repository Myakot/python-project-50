import pytest


from gendiff.generate_difference import generate_diff, get_format_and_data
from gendiff.formatters import stringify_diff
from tests.utils import get_file_path
from tests.CONSTANTS import PATH_JSON_FLAT_RESULT


def get_file_data(result_name):
    with open(f'tests/fixtures/{result_name}') as file:
        return file.read()

format_cases = {'yml', 'json'}
result_flat_stylish = get_result('results/result_flat_stylish')
result_flat_plain = get_result('results/result_flat_plain')
result_flat_json = get_result('results/result_flat_json')

@pytest.mark.parametrize('format_case', format_cases)
def test_gendiff_flat(format_case):
    file_paths = get_file_data(f'flat1.{format_case}'), get_file_data(f'flat2.{format_case}')
    assert generate_diff(*file_paths) == result_flat_stylish
    assert generate_diff(*file_paths, FORMATS.STYLISH) == result_flat_stylish
    assert generate_diff(*file_paths, FORMATS.PLAIN) == result_flat_plain
    assert generate_diff(*file_paths, FORMATS.JSON) == result_flat_json


@pytest.mark.parametrize(
    "file1_path, file2_path, path_to_result",
    [
        pytest.param(
            'file_1_flat.yml',
            'file_2_flat.yaml',
            'file_flat_result_yaml',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file_1_1.json',
            'file_1_2.json',
            'file_1_result_json',
            id="json_file"
        ),
        pytest.param(
            'file_2_1.json',
            'file_2_2.json',
            'file_2_result_json',
            id="json_2_file"
        ),
    ],
)
def test_generate_diff(file1_path, file2_path, path_to_result):
    expected_path = get_file_path(path_to_result)
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_file_path(file1_path)
        test_path2 = get_file_path(file2_path)
        assert generate_diff(test_path1, test_path2) == result_data


@pytest.mark.parametrize(
    "file1_path, file2_path, print_format,  path_to_result",
    [
        pytest.param(
            'file_1_1.yml',
            'file_1_2.yaml',
            'stylish',
            'file_1_result_json',
            id="yml_yaml_stylish"
        ),
        pytest.param(
            'file_1_1.yml',
            'file_1_2.yaml',
            'json',
            'file_1_format.json',
            id="yaml_to_json"
        ),
        pytest.param(
            'file_1_1.yml',
            'file_1_2.yaml',
            'plain',
            'file_1_result_plain',
            id="yaml_to_plain"
        ),
        pytest.param(
            'file_1_1.json',
            'file_1_2.json',
            'plain',
            'file_1_result_plain',
            id="json_plain_file"
        ),
        pytest.param(
            'file_2_1.json',
            'file_2_2.json',
            'plain',
            'file_2_plain_result',
            id="json_2_plain_file"
        ),
        pytest.param(
            'file_1_1.json',
            'file_1_2.json',
            'json',
            'file_1_format.json',
            id="json_format_file"
        ),
        pytest.param(
            'file_2_1.json',
            'file_2_2.json',
            'json',
            'file_2_format.json',
            id="json_2_format_file"
        ),
    ],
)
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
