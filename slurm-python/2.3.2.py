# Методы строк

if __name__ == '__main__':
    # lstrip - Обрезка символов слева
    print('---Text---'.lstrip('-'))
    # rstrip - Обрезка символов справа
    print('---Text---'.rstrip('-'))
    # strip  - Обрезка символов
    print('---Text---'.strip('-'))

    # upper - привести к верхнему регистру
    print('this is a Text'.upper())
    # lower - привести к нижниму регистру
    print('This is a Text'.lower())
    # capitalize - Привести первую букву к верхнему регистру
    print('this is a Text'.capitalize())

    # replace - заменить одну подстроку на другую
    print('This is a text'.replace('text', 'string'))
    print('This is a text'.replace('t', 'k'))
    print('This is a text'.replace('t', 'k', 1))

    # Индексы
    # Я(0) (1)с(2)т(3)р(4)о(5)к(6)а(7) - прямая индексация
    # Я(-8) (-7)с(-6)т(-5)р(-4)о(-3)к(-2)а(-1)

    # Срез - возможность извлечь из строки какую-либо подстроку

    # [A:B] - вывести срез с позиции А по В, не включая В
    print('0123456'[2:5]) # > 234
    # [A:] - вывести срез с позиции А до конца
    print('0123456'[2:]) # > 23456
    # [:B] - вывести срез с начала по позиции В, не включая В
    print('0123456'[:5]) # > 01234

    # Срезы в обратной индексации
    print('0123456'[2:-2]) # > 234
    print('0123456'[-5:])  # > 23456
    print('0123456'[:-2])  # > 01234

    # Срез с шагом
    # [A:B:STEP] - вывести срез с позиции А по В, не включая В, с шагом STEP
    print('0123456'[:6:3])  # > 03
    print('0123456'[2:6:2]) # > 24

    # Practice 1

    # TODO: Вывести строку с интерполированными переменными
    # TODO: Убрать пробелы в начале и конце имени
    # TODO: Убрать символы '~' в начале и конце имени
    # TODO: Сделать первую букву имени заглавной
    # TODO: Привести профессию к нижнему регистру
    # TODO: Заменить в адресе эл. почты символ '@' на предлог 'at'
    # TODO: Разгадать и вывести секретный символ

    name  = '     ~~~вячеслав~~~   '
    job   = 'Инженер'
    email = 'example@domain.com'

    secret_symbol_first_part  = 'wer4605rtrt'
    secret_symbol_second_part = 'w5g3t3g2j'
    secret_symbol             = chr(int(secret_symbol_first_part[3:7]) + int(secret_symbol_second_part[1::2]))

    result = (f'Меня зовут {name.strip(" ~").capitalize()}, я {job.lower()}, '
              f'пишите мне на {email.replace("@", " at ")}'
              f'{secret_symbol}')
    print(result)

    # Practice 2
    platform = 'K8s'
    atomic_unit = 'POD'
    what_about_kubernetes = 'Минимальной единицей является'
    # TODO: Получить строку 'Минимальной единицей Kubernetes является pod'
    platform = platform.replace('8', 'ubernete')
    result_2 = f'{what_about_kubernetes.replace("й я", f"й {platform} я")} {atomic_unit.lower()}'
    print(result_2)

    # Practice 3
    introduction_name = 'Disaster recovery plan'
    print(introduction_name[9:-5])  # > recovery
    print(introduction_name[9:])    # > recovery plan
    print(introduction_name[:8])    # > Disaster





