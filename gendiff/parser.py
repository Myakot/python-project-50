import json
import os.path
import yaml

from yaml.loader import SafeLoader



def file_parser(file_path):
    file_extension = os.path.splitext(file_path)[1].lstrip('.')
    with open(file_path) as file:
        if file_extension.lower() == 'json':
            return json.load(file)
        elif (file_extension.lower() == 'yaml') or (
                file_extension.lower() == 'yml'):
            return yaml.load(file, Loader=SafeLoader)
        else:
            print(f"File with unknown extension: {file_path}")
