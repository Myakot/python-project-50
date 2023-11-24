import json
from os.path import normpath
from gendiff.parser import file_parser


def run_gendiff(file_path1, file_path2):
    file_path1 = normpath(file_path1)
    file_path2 = normpath(file_path2)
    data1 = file_parser(file_path1)
    data2 = file_parser(file_path2)
    print(generate_diff(data1, data2))


def generate_diff(data1, data2):
    diff = {}

    for key in data1.keys():
        item1 = data1[key]

        if key not in data2.keys():
            diff[f'- {key}'] = item1
        elif item1 == data2[key]:
            diff[f' {key}'] = data2.pop(key)
        else:
            diff[f'- {key}'] = item1

    if data2:
        diff.update({f'+ {key}': item for key, item in data2.items()})

    sorted_diff = dict(sorted(diff.items(), key=lambda x: x[0][2:]))

    return format_diff(sorted_diff)


def format_diff(diff):
    json_diff = json.dumps(diff, indent=2, separators=('', ': '))
    return (str(json_diff)).replace('"', '')
