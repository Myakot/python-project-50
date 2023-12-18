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
        ValueError: If the data is empty.
    """
    if not data or data.strip() == '':
        raise ValueError('Data is empty')
    match format:
        case 'json':
            return json.loads(data)
        case 'yaml':
            return yaml.load(data, yaml.Loader)
        case 'yml':
            return yaml.load(data, yaml.Loader)
        case _:
            raise ValueError(f"Invalid format: {format}")
