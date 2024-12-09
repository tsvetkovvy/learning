# Логический тип данных

if __name__ == '__main__':
    one_and_half = 1.5
    two = 2
    slurm = 'Slurm'
    localized_slurm = 'Слёрм'
    print(one_and_half == two)
    # print(type(one_and_half))
    # print(type(slurm))

    # NOT
    is_python_easy = True
    print(not is_python_easy)

    # OR
    print(bool(1 + 1)) # > True
    print(bool(1 + 0)) # > True
    print(bool(0 + 1)) # > True
    print(bool(0 + 0)) # > False

    # AND
    print(bool(1 * 1)) # > True
    print(bool(1 * 0)) # > False
    print(bool(0 * 1)) # > False
    print(bool(0 * 0)) # > False

    # Practice 1
    my_name = 'Хикматилло'
    print(ord(my_name[0])) # > 1061
    is_my_name_long = my_name == 8
    print(is_my_name_long)

    # Practice 2
    free_ram_amount = 200
    app_replicas = 2
    has_ram_overdraft = True
    balance = 10000

    is_enough_money = balance > 8000
    is_enough_ram = free_ram_amount / app_replicas >= 150
    print(is_enough_money or is_enough_ram)


