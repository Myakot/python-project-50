from gendiff.engine import run_gendiff


def test_generate_diff():
    result = open('tests/fixtures/correct.json')
    assert run_gendiff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == print(result)


def test_generate_diff_yaml():
    result = open('tests/fixtures/correct.json')
    assert run_gendiff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == print(result)
