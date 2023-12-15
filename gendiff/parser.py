import yaml
import json


def parse(data: str, format: str) -> dict:
    """
    Parses the given data using the specified format and returns
    the parsed result as a dictionary.

    Parameters:
        data (str): The data to be parsed.
        format (str): The format of the data. Valid options are
        'json', 'yaml', and 'yml'.

    Returns:
        dict: The parsed data as a dictionary.

    Raises:
        TypeError: If the data is empty.
    """
    if not data:
        raise TypeError('File is missing data')
    match format:
        case 'json':
            return json.loads(data)
        case 'yaml':
            return yaml.load(data, yaml.Loader)
        case 'yml':
            return yaml.load(data, yaml.Loader)
