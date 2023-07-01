# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def create_dictionary(**kwargs):
    argument_dict = {}

    for key, value in kwargs.items():
        try:
            hash(key)
        except TypeError:
            key = str(key)

        argument_dict[key] = value

    return argument_dict


result = create_dictionary(a=1, b=2, c=3)
print(result)
