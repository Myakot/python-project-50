import yaml
import json


def parse(data: str, format: str) -> dict:
    if data and format == 'json':
        return json.loads(data)
    elif data and format == 'yml':
        return yaml.load(data, yaml.Loader)
    else:
        raise FileNotFoundError(f"Unknown file format: {format}")
