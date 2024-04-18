# Словари

if __name__ == '__main__':
    # Инициализация словаря
    info_about_me = {'name': 'Viacheslav', 'temperature': 23, 'humidity': 44}
    # Получение значения
    print(info_about_me['name']) # > Viacheslav
    # Добавление значения
    info_about_me['is_i_love_python'] = True
    print(info_about_me)
    # Перезапись значения
    info_about_me['humidity'] = 50
    print(info_about_me)
    # Метод get
    print(info_about_me.get('temperature')) # > 23
    print(info_about_me.get('temperature_2')) # > None
    print(info_about_me.get('temperature_2', 0)) # > 0
    # Метод items
    print(list(info_about_me.items()))
    for k, v in info_about_me.items():
        print(k, v, sep=':')
    # Метод keys
    print(list(info_about_me.keys()))
    # Метод values
    print(list(info_about_me.values()))
    # Метод update
    info_about_me.update({'temperature': 26, 'cat_count': 0})
        # temperature обновится, cat_count создастся
    print(info_about_me)
    # Метод popitem
    pair = info_about_me.popitem()
    print(pair) # > ('cat_count', 0)
    print(info_about_me) # > {'name': 'Viacheslav', 'temperature': 26, 'humidity': 50, 'is_i_love_python': True}
    # Метод pop
    value = info_about_me.pop('humidity')
    print(value) # > 50
    print(info_about_me) # > {'name': 'Viacheslav', 'temperature': 26, 'is_i_love_python': True}
    # Метод clear
    # print(info_about_me.clear())
    # Метод copy
    copy_info_about_me = info_about_me.copy()
    copy_info_about_me['cat_count'] = 0
    print(info_about_me)
    print(copy_info_about_me)
    # Метод setdefault
    value = info_about_me.setdefault('surname', 'Tsvetkov') # Второе значение - по умолчанию
    print(value)
    print(info_about_me)
    # Метод fromkeys
    my_dict = dict.fromkeys(['first', 'second', 3], 'Hello I\'m fromkeys')
    print(my_dict)
    # Создание словаря из последовательности
    # my_list = [('first', 1), ('second', 2), ('third', 3)]
    # print(dict(my_list))
    my_keys = ['first', 'second', 'third']
    my_values = [1, 2, 3]
    print(dict(zip(my_keys, my_values)))


