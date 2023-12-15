def create_diff(data_1: dict, data_2: dict) -> list:
    """
    Generates a diff between two dictionaries.

    Parameters:
    - data_1 (dict): The first dictionary to compare.
    - data_2 (dict): The second dictionary to compare.

    Returns:
    - diff (list): A list of differences between the two dictionaries. Each difference is represented as a dictionary with the following keys:
        - name (str): The name of the key that has a difference.
        - type (str): The type of difference. Possible values are:
            - 'added': The key is present in data_2 but not in data_1.
            - 'removed': The key is present in data_1 but not in data_2.
            - 'nested': The key is present in both dictionaries and its value is a nested dictionary. The nested dictionary represents the differences in the values of the key.
            - 'unchanged': The key is present in both dictionaries and its value is the same in both.
            - 'changed': The key is present in both dictionaries and its value is different in data_1 and data_2. The value is a tuple containing the old value from data_1 and the new value from data_2.
        - value: The value associated with the key.

    """
    diff = []

    keys = data_1.keys() | data_2.keys()

    for key in sorted(keys):
        new_item = {'name': key}

        if key not in data_1:
            new_item.update({
                'type': 'added', 'value': data_2[key]
            })
        elif key not in data_2:
            new_item.update({
                'type': 'removed', 'value': data_1[key]
            })
        else:
            value_1, value_2 = data_1[key], data_2[key]
            if isinstance(value_1, dict) and isinstance(value_2, dict):
                new_item.update({
                    'type': 'nested', 'children': create_diff(value_1, value_2)
                })
            elif value_1 == value_2:
                new_item.update({
                    'type': 'unchanged', 'value': value_1
                })
            else:
                new_item.update({
                    'type': 'changed', 'value': (value_1, value_2)
                })
        diff.append(new_item)

    return diff
