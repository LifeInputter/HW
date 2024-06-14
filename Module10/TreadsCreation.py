# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.

import threading
import time
import  string
from threading import Thread
from time import sleep

#var1
def count():
    x = []
    for x in range(1,11):
        print(x, flush=True)
        time.sleep(1)

def show_letters():
    s = string.ascii_lowercase
    symbols_to_remove = "klmnopqrstuvwxyz"
    for symbol in symbols_to_remove:
        s = s.replace(symbol,'')
    for i in s:
        print(i)
        time.sleep(1)
#

# # map(for x, i in count(),show_letters()):
#
thread1 = threading.Thread(target=count())
thread2 = threading.Thread(target=show_letters())


thread1.start()
thread2.start()

thread1.join()
thread2.join()


# for x, y in count(), show_letters():
#     print(x, y)

#var.2
print("-"*10, "var.2", "-"*10)

def function1():
    for i in range(1,11):
        print(i,""*5, flush=True)
        time.sleep(1)


def function2():
    for letter in 'abcdefghij':
        print(letter, flush=True)
        time.sleep(1)


thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# print(string.ascii_lowercase)