import yaml
import json


def parse(data: str, format: str) -> dict:
    if not data:
        raise TypeError('File is missing data')
    match format:
        case 'json':
            return json.loads(data)
        case 'yaml':
            return yaml.load(data, yaml.Loader)
        case 'yml':
            return yaml.load(data, yaml.Loader)
