# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonachi_gen(n):
    num1 = 0
    num2 = 1
    for i in range(1, n + 1):
        num2 += num1
        yield num1
        num1 = num2 - num1


for num in fibonachi_gen(10):
    print(f'{num}', end=" ")