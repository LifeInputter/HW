import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for num in range(1, 6):
        print(f"Силач {name} поднял шар {num}")
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Victor", 3))
    task2 = asyncio.create_task(start_strongman('Narzan', 4))
    task3 = asyncio.create_task(start_strongman('Sub-zero', 5))
    await task1
    await task2
    await task3
    # var.2
    # participants = [("Victor", 3), ("Narzan", 4), ("Sub-zero", 5)]
    #
    # tasks = [start_strongman(name, power) for name, power in participants]
    #
    # await asyncio.gather(*tasks)


asyncio.run(start_tournament())

''''
Задача "Асинхронные силачи":
Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность. 
Реализуйте следующую логику в функции:
В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его силе power.
 Для каждого участника количество шаров одинаковое - 5.
В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman. 
Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
После поставьте каждую задачу в ожидание (await).
Запустите асинхронную функцию start_tournament методом run.

'''''
