# Кортежи

if __name__ == '__main__':
    trash_can = ('Viacheslav', True, 0)
    climate = (21, 53)

    # Распаковка кортежа
    # name, is_i_love_python, cat_count = trash_can
    cat_count, temperature, humidity = (trash_can + climate)[2:]
    print(cat_count, temperature, humidity)

    name = 'Bob'
    a, b, c = name
    print(a, b, c) # > B o b


    # print(trash_can + climate) # Конкатенация кортежей
    # print(trash_can[:2])       # Срез кортежа
    # print(name, is_i_love_python, cat_count) # Распаковка кортежа

    # Practice
    basic_cources = ('Docker', 'Ansible', 'Ceph')
    advanced_cources = ('Kubernetes База', 'Kubernetes Мега')
    print((basic_cources + advanced_cources)[1::3]) # > ('Ansible', 'Kubernetes Мега')




