from json import dumps


def json_format(diff: list) -> str:
    return dumps(diff, sort_keys=True, indent=2)
# Тут же значения и так отсортированы у нас, можно опустить указание сортировки
