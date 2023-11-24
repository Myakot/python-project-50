from gendiff.engine import run_gendiff
import pytest


def test_generate_diff():
    answer = open('tests/fixtures/correct.json')
    assert run_gendiff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == print(answer)
