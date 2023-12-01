import pytest
import copy

from gendiff.generate_difference import generate_diff, open_
from gendiff.parser import parse
from gendiff.diff import create_diff
from formatters.stylish import stylish_format
from formatters.plain import plain_format
from formatters.json import json_format
from gendiff.formatter import stringify_diff
import tests.CONSTANTS as path


# В очередной раз спасибо комментариям к шагам проекта за декоратор parametrize
@pytest.mark.parametrize('file1_path, file2_path, path_to_result',
                         [(path.PATH_JSON_FLAT_1, path.PATH_JSON_FLAT_2, path.PATH_JSON_FLAT_RESULT),
                          (path.PATH_YML_FLAT_1, path.PATH_YML_FLAT_2, path.PATH_YML_FLAT_RESULT),
                          (path.PATH_JSON_1_1, path.PATH_JSON_1_2, path.PATH_JSON_1_RESULT),
                          (path.PATH_JSON_2_1, path.PATH_JSON_2_2, path.PATH_JSON_2_RESULT)])
def test_generate_diff(file1_path, file2_path, path_to_result):
    with open(path_to_result) as result_file:
        assert generate_diff(file1_path, file2_path) == result_file.read()


@pytest.mark.parametrize('file1_path, file2_path, print_format, path_to_result',
                         [(path.PATH_YML_1, path.PATH_YML_2, 'stylish', path.PATH_YAML_RESULT),
                          (path.PATH_YML_1, path.PATH_YML_2, 'plain', path.PLAIN_1_RESULT),
                          (path.PATH_YML_1, path.PATH_YML_2, 'json', path.JSON_FORMAT_RESULT_1),
                          (path.PATH_JSON_1_1, path.PATH_JSON_1_2, 'plain', path.PLAIN_1_RESULT),
                          (path.PATH_JSON_2_1, path.PATH_JSON_2_2, 'plain', path.PLAIN_2_RESULT),
                          (path.PATH_JSON_1_1, path.PATH_JSON_1_2, 'json', path.JSON_FORMAT_RESULT_1),
                          (path.PATH_JSON_2_1, path.PATH_JSON_2_2, 'json', path.JSON_FORMAT_RESULT_2)])
def test_generate_diff_format(file1_path, file2_path, print_format, path_to_result):
    with open(path_to_result) as result_file:
        assert generate_diff(file1_path,
                             file2_path,
                             print_format) == result_file.read()


def test_open_exception():
    with pytest.raises(FileNotFoundError):
        open_(path.PATH_JSON_FLAT_RESULT)


def test_parse_exception():
    with pytest.raises(FileNotFoundError):
        parse('something', 'unknown format')


def test_stringify_exception():
    with pytest.raises(FileNotFoundError):
        stringify_diff('diff_data', 'unknown format')


def test_diff():
    data_1 = parse(*open_(path.PATH_JSON_1_1))
    data_1_copy = copy.deepcopy(data_1)
    data_2 = parse(*open_(path.PATH_JSON_1_2))
    data_2_copy = copy.deepcopy(data_2)
    create_diff(data_1, data_2)
    assert data_1 == data_1_copy
    assert data_2 == data_2_copy


def test_print():
    data_1 = parse(*open_(path.PATH_JSON_1_1))
    data_2 = parse(*open_(path.PATH_JSON_1_2))
    diff = create_diff(data_1, data_2)
    diff_copy = copy.deepcopy(diff)
    stylish_format(diff)
    plain_format(diff)
    json_format(diff)
    assert diff == diff_copy
