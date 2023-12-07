import yaml
import json


def parse(data: str, format: str) -> dict:
    if data and format == 'json':
        return json.loads(data)
    else:
        return yaml.load(data, yaml.Loader)
