# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег. Необходимо
# использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
# Используйте класс Lock из модуля threading для блокировки доступа к общему ресурсу.
# Ожидается создание двух потоков, один для пополнения счета, другой для снятия денег.
# Используйте with (lock object): в начале каждого метода, чтобы использовать блокировку

import threading
from threading import Thread
from threading import Lock
from collections import defaultdict

lock = threading.Lock()


class BankAccount(threading.Thread):
    def __init__(self, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.account = account
        # self.balance = defaultdict
        self.new_balance = defaultdict
        self.start_balance = 1000
        self.account_lock = lock()

    # def run(self):
    #     self.start_balance = 1000

    def deposit_task(self, account, amount):
        with self.account_lock:
            self.new_balance = self.start_balance
            for _ in range(5):
                self.new_balance += amount

                # return self.new_balance
                # self.balance.update(self.new_balance)
                # print(self.balance)
                print(f'Deposited {amount}, new balance is {self.new_balance}', flush=True)

    def withdraw_task(self, account, amount):
        with self.account_lock:
            # self.balance = defaultdict(int)
            for _ in range(5):
                self.new_balance -= amount
                print(f'Withdrew {amount}, new balance is {self.new_balance}', flush=True)


account = BankAccount(lock=threading.Lock)

deposit_thread = threading.Thread(target=account.deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=account.withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
