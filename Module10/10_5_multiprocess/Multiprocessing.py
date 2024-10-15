import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            for line in file:
                if not line:
                    break
                else: all_data.append(line)
                return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start = datetime.datetime.now()
# for file in filenames:
#     read_info(file)
# end = datetime.datetime.now()
# print(f'{end - start} (линейный)')


# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')

# results:
#0:00:00.417001 (линейный)
#0:00:00.199831 (многопроцессный)

'''
Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool.
Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время 
выполнения и выведите его в консоль.
'''