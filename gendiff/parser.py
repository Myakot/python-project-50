import yaml
import json


def parse(data: str, format: str) -> dict:
    match format:
        case 'json':
            return json.loads(data)
        case 'yaml':
            return yaml.load(data, yaml.Loader)
        case 'yml':
            return yaml.load(data, yaml.Loader)
