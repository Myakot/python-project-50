from gendiff.engine import run_gendiff
import pytest


def test_generate_diff():
    answer = open('gendiff/files/correct.json')
    assert run_gendiff('gendiff/files/file1.json', 'gendiff/files/file2.json') == print(answer)
