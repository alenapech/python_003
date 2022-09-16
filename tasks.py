#1. Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
print('task_001')
l = int(input('Введите длину списка: '))
some_list = [int(input ('Введите список:')) for _ in range (l)]
print(some_list)
sum = 0
for i in range(1, len(some_list), 2):
    sum += some_list[i]
print(sum)

#2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
print('task_002')
l = int(input('Введите длину списка: '))
some_list = [int(input ('Введите список:')) for _ in range (l)]
print(some_list)
new_list = []
for i in range(len(some_list) // 2 + len(some_list) % 2):
    new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
print(new_list)

#3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.
print('task_003')
l = int(input('Введите длину списка: '))
some_list = [float(input ('Введите список:')) for _ in range (l)]
new_list = [float('0.' + str(i).split('.')[1]) for i in some_list if '.' in str(i)]
print(new_list)
print(max(new_list) - min(new_list))

#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print ('task_004')
n = int(input('Введите число: '))
some_str = ''
if n < 0 or n == 0:
    n = int(input('Введите положительное число отличное от 0: '))
while n > 0:
    some_str = str(n%2) + some_str
    n //=2
print(some_str)

#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
print('task_005')
k = int(input('Введите число для рядя Фибоначчи: '))
fibonaccilist = [0]*(k*2+1)
fibonaccilist[k] = 0
fibonaccilist[k+1] = 1

for i in range(k+2, len(fibonaccilist)):
    fibonaccilist[i] = fibonaccilist[i-2] + fibonaccilist[i - 1]

for i in range(k, -1, -1):
    fibonaccilist[i] = fibonaccilist[i+2] - fibonaccilist[i+1]

print(fibonaccilist)
