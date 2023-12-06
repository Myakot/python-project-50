
# Здесь функция создает разницу между двумя словарями.
# Функция проверяет наличие разных ключей, общих
# ключей и разницу между значениями.
# Если значение является вложенным словарем, функция рекурсивно вызывает
# себя для создания разницы между этими вложенными словарями

# Интересное решение данного момента, а что на счет?
# keys = data_1.keys() | data_2.keys()
# А дальше обходить их предварительно отсортировав, сравнивая,
# есть ли итерируемый key в data_1 или data_2? Что думаешь?

def create_diff(data_1: dict, data_2: dict) -> list:
    added_names, removed_names = (set(data_1) - set(data_2),
                                  set(data_2) - set(data_1))
    common_names = set(data_1) & set(data_2)
    result = list()
    names = list(added_names | removed_names | common_names)
    for name in sorted(names):
        new_item = {'name': name}
        if name in added_names or name in removed_names:
            new_item['type'] = 'removed' if name in added_names else 'added'
            new_item['value'] = \
                data_1[name] if name in added_names else data_2[name]
            result.append(new_item)
            continue
        value_1, value_2 = data_1[name], data_2[name]
        if isinstance(value_1, dict) and isinstance(value_2, dict):
            new_item['type'] = 'nested'
            new_item['children'] = create_diff(value_1, value_2)
        elif value_1 == value_2:
            new_item['type'] = 'unchanged'
            new_item['value'] = value_1
        else:
            new_item['type'] = 'changed'
            new_item['value'] = value_1, value_2
        result.append(new_item)
    return result
