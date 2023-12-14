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

# Понял твою задумку, но тогда если у нас не будет даты, а формат json, то тогда и там нужно проверять наличие даты.
# Можно сделать проверку в начале if not data с исключением, а если есть - то тогда уже загружать по нахождению кейсов
