# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def patcher(pathFile: str):
    a, b = os.path.split(pathFile)
    b, c = b.split('.')
    return (a, b, c)


pathFile = "C:\Учеба_GB\DataEngineer\Python\Sem5\Work1.py"
print(patcher(pathFile))
