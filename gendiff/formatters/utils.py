import os


def get_key_info(item: dict) -> tuple:
    name = item.get('name')
    type_ = item.get('type')
    value = item.get('value')
    return name, type_, value


def get_children(item: dict) -> list:
    return item.get('children')


def get_file_data(file_name):
    file_path = os.path.join(os.getcwd(), 'fixtures', file_name)

    with open(file_path, 'r') as file:
        return file.read()
