def create_diff(data_1: dict, data_2: dict) -> list:
    diff = []

    keys = data_1.keys() | data_2.keys()

    for key in sorted(keys):
        new_item = {'name': key}

        if key not in data_1:
            new_item['type'] = 'added'
            new_item['value'] = data_2[key]
        elif key not in data_2:
            new_item['type'] = 'removed'
            new_item['value'] = data_1[key]
        else:
            value_1, value_2 = data_1[key], data_2[key]
            if isinstance(value_1, dict) and isinstance(value_2, dict):
                new_item['type'] = 'nested'
                new_item['children'] = create_diff(value_1, value_2)
            elif value_1 == value_2:
                new_item['type'] = 'unchanged'
                new_item['value'] = value_1
            else:
                new_item['type'] = 'changed'
                new_item['value'] = value_1, value_2
        diff.append(new_item)

    return diff
