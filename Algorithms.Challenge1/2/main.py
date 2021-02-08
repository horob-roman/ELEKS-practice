#Задача 2. Algorithms. Challenge №1
#Хороб Роман КІ-19-1К
fib1 = 1
fib2 = 1

n = input("Введіть індекс числа з ряду Фібоначчі: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)
