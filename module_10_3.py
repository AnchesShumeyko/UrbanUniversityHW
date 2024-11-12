import threading
from random import randint
from time import sleep

'''"Банковские операции"'''


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            replenishment = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            request = randint(50, 500)
            print(f'Запрос на {request}')
            if request <= self.balance:
                self.balance -= request
                print(f'Снятие: {request}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')