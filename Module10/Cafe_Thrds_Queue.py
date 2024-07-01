# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, is_busy(bool) - занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)
#
# Пример работы:
# # Создаем столики в кафе
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
# tables = [table1, table2, table3]
#
# # Инициализируем кафе
# cafe = Cafe(tables)
#
# # Запускаем поток для прибытия посетителей
# customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
#
# # Ожидаем завершения работы прибытия посетителей
# customer_arrival_thread.join()

import queue
import threading
import time
from threading import Thread

class Table(Thread):
    def __init__(self, number, is_busy=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number
        self.is_busy = is_busy


class Cafe(Thread):
    def __init__(self, tables, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue_customers = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            time.sleep(1)
            print(f'Посетитель номер {i} прибыл')
            self.queue_customers.put(i)
            print(f'Посетитель номер {i} ожидает свободный стол', flush=True)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                # print(f'Посетитель {customer} номер ожидает свободный стол', flush=True)
                print(f'Посетитель номер {customer} сел за стол {table.number}', flush=True)
                time.sleep(5)
                print(f'Посетитель номер {customer} покушал и ушел', flush=True)
                table.is_busy = False
                self.queue_customers.get(customer)
                if cafe.queue_customers.empty():
                    print("-" * 20) # индикатор пустой очереди
                    break

                # print(f'Посетитель номер {customer} сел за стол {table.number}', flush=True)
            # table.is_busy = True
            #  time.sleep(5)
            #  print(f'Посетитель номер {customer} покушал и ушел', flush=True)
            #     table.is_busy = False
            # else:
            #     return print(f'Посетитель {customer} номер ожидает свободный стол', flush=True)
            #     self.queue_customers.put(customer)
            # print(f'Посетитель {customer} номер ожидает свободный стол', flush=True)
        self.queue_customers.put(customer)

    def customer_thread(cafe):
        while True:
            customer = cafe.queue_customers.get()
            cafe.serve_customer(customer)
            cafe.queue_customers.task_done()
            if cafe.queue_customers.empty():
                break


# class Customer(Thread):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

# def run(cafe):
#     while True:
#         customer = cafe.queue_customers.get()
#         cafe.serve_customer(customer)
#         cafe.queue_customers.task_done()
#         if cafe.queue_customers.empty():
#             break
#


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

for _ in range(3):
    t = threading.Thread(target=cafe.customer_thread)
    t.start()
t.join()

customer_arrival_thread.join()
