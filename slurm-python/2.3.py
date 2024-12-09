# Строки

if __name__ == '__main__':
    name = 'Вячеслав'
    job = 'инженер'
    email = 'example@domain.com'

    # who_am_i = 'Меня зовут {}, я {}, пишите мне на {}'.format(name, job, email)
    # who_am_i = f'Меня зовут {{}} {name}, я {job}, пишите мне на {email}' # {{}} - экранирование
    who_am_i = f'Меня зовут {name:>30}, я {job}, пишите мне на {email}' # 30 отступов перед переменной name

    print(who_am_i)

    # Practice
    pod_name = 'Pod'
    replicaset_name = 'ReplicaSet'
    kubernetes_structures_desc = f'Для объединения нескольких контейнеров в одну минимальную единицу используется {pod_name}, в то время как {replicaset_name} контролирует количество реплик приложения'
    print(kubernetes_structures_desc)
