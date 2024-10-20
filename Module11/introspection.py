import inspect
from pprint import pprint

def introspection_info(obj):
    type_obj = type(obj).__name__  #Определение типа объекта
    list_dir = dir(obj)
    attributes = [obj,'__dict__']
    methods = []
    for i in list_dir:
        if callable(getattr(obj, i)) is True:
            methods.append(i)   #Получение методов объекта
        else:
            attributes.append(i)   #Получение атрибутов объекта
    module = obj.__class__.__module__      #Определение модуля, к которому объект принадлежит
    func = inspect.isfunction(obj)
    #Создание словаря с информацией об объекте
    info = {'type': type_obj, 'attributes': attributes, 'methods': methods, 'module': module, 'function': func}
    return (info)

number_info = introspection_info(12) # Интроспекция чисел
pprint(number_info)

print("<>"*30)

string_info = introspection_info("poetry") #интроспекция строк
pprint(string_info)

print("<>"*30)

list_info = introspection_info([1,3,"78", bool]) #интронспекция списков
pprint(list_info)

"""
Д/З ИНТРОСПЕКЦИЯ

Создать персональную функции для подробной интроспекции объекта.
1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""