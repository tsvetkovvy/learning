# Прерывания в циклах

if __name__ == '__main__':

    # TODO: Получать эл. почту и профессию сотрудника
    # TODO: Сформировать список систем, в которые будет предоставлен доступ и вывести на экран сообщение с этим списком
    # TODO: Программист работает в СКВ
    # TODO: Дизайнер работает в иллюстраторе
    # TODO: Сантехнику не нужны доступы
    # TODO: Должна быть возможность выдать права нескольким сотрудникам за один запуск
    # TODO: Доступ в иллюстратор выдается только с третьего раза
    # TODO: За один запуск нельзя добавлять более пяти новых сотрудников, о лимитах нужно оповестить

    processed_employees = 0
    while processed_employees < 5:
        print('Введите email')
        email = input()
        if email == '':
            print('Ввод прерван')
            break
        print('Введите профессию')
        job = input()

        system = None
        access_attempts = None

        if job == 'Программист':
            system = 'СКВ'
            access_attempts = 1
        elif job == 'Дизайнер':
            system = 'Иллюстратор'
            access_attempts = 3
        else:
            print('АХО через три двери направо')
            continue

        for _ in range(access_attempts):
            print(f'{email} бьл выдан доступ в {system}')

        processed_employees += 1
        print(f'Было внесено {processed_employees} сотрудников, осталось {5 - processed_employees}')
