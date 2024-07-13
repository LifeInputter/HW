import threading
from queue import Queue
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            customer = f'Посетитель номер {i}'
            print(f'{customer} прибыл')
            self.serve_customer(customer)
            time.sleep(1)

    # serve_customer: Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока),
    # в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.

    def serve_customer(self, customer):
        free_table = next((table for table in self.tables if not table.is_busy), None)
        if free_table:
            free_table.is_busy = True
            print(f'{customer} сел за стол {free_table.number}')
            customer_thread = threading.Thread(target=self.customer_dining, args=(customer, free_table))
            customer_thread.start()

        else:
            print(f'{customer} ожидает свободный стол') # помещение в очередь
            self.queue.put(customer)

    def customer_dining(self, customer, table):
        time.sleep(5)
        print(f'{customer} покушал и ушел')
        table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.join()
            self.serve_customer(next_customer)



class Customer(threading.Thread):
    def __init__(self, cafe, name, ):
        super().__init__()
        self.cafe = cafe
        self.name = name
    def run(self):
        while True:
            self.cafe.customer_arrival()



table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables) #инициализируем кафе

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
