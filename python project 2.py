try:
    value_1 = my_dict[key_1]
    value_2 = my_dict[key_2]
    value_1, value_2 = float(value_1), float(value_2)
    new_value = value_1 + value_2
except KeyError:
    print('Введен неверный ключ')
except ValueError:
    print('Неверное преобразование типов')