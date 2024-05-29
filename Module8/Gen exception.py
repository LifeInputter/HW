# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception. Например, InvalidDataException
# и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте


class InvalidData(Exception):
    pass

def new_customer(name):
    if name == "SonOfBitch":
        raise InvalidData('Введено неподходящее имя', name)

    print(f'{name}, рады видеть Вас среди наших клиентов!')
try:
    new_customer("SonOfBitch")  # "SonOfBitch"   "Vladimir"
except InvalidData as e:
    print(f"Перехвачена ошибка:\n {type(e)},{e.args}\n")


class Processing(Exception):
    def __init__(self, message):
        self.message = message


def average_transaction_summ(vollume, number_of_cards):
    if number_of_cards == 0:
        raise Processing("Деление на ноль невозможно")
    if number_of_cards < 0:
        raise Processing('количество карт не может быть отрицательным')
    return vollume // number_of_cards


try:
    result = average_transaction_summ(1250000, -45)
    print(f'Усредненный объем транзакции по карте составил: {result}  руб.')

except Processing as exc:
    print("Возникла ошибка при обработке данных")
    print(f'Сообщение об ошибке: {exc.message}')

# new_customer('SonOfBitch')
