import pytest
import copy
import os


from gendiff.generate_difference import generate_diff, get_format_and_data
from gendiff.parser import parse
from gendiff.diff_tree import create_diff
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import json_format
from gendiff.formatters import stringify_diff
from gendiff.utils import get_file_path
import tests.CONSTANTS as PATH


@pytest.mark.parametrize(
    "file1_path, file2_path, path_to_result",
    [
        pytest.param(
            'file_1_flat.json',
            'file_2_flat.json',
            'file_flat_result_json',
            id="flat_json_file"
        ),
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
        get_format_and_data(PATH.PATH_JSON_FLAT_RESULT)


def test_stringify_exception():
    with pytest.raises(ValueError):
        stringify_diff('diff_data', 'unknown format')


def test_diff():
    data_1 = parse(*get_format_and_data(PATH.PATH_JSON_1_1))
    data_1_copy = copy.deepcopy(data_1)
    data_2 = parse(*get_format_and_data(PATH.PATH_JSON_1_2))
    data_2_copy = copy.deepcopy(data_2)
    create_diff(data_1, data_2)
    assert data_1 == data_1_copy
    assert data_2 == data_2_copy


def test_print():
    data_1 = parse(*get_format_and_data(PATH.PATH_JSON_1_1))
    data_2 = parse(*get_format_and_data(PATH.PATH_JSON_1_2))
    diff = create_diff(data_1, data_2)
    diff_copy = copy.deepcopy(diff)
    stylish_format(diff)
    to_plain(diff)
    json_format(diff)
    assert diff == diff_copy
