# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import os
# os.system('clear')

# def ask_number_list():
#     str_list = input('Введите числа через пробел: ').split(' ')
#     number_list = []
#     for val in str_list:
#         if(val.isdigit()):
#             number_list.append(int(val))
#     return number_list

# def sum_odd_numbers(list_numbers):
#     sum = 0
#     for i,val in enumerate(list_numbers):
#         if(not i%2 == 0):
#             sum += val
#     return sum

# numbers = ask_number_list()
# print(f'{numbers} -> сумма элементов на нечетной позиции = {sum_odd_numbers(numbers)}') 





# 2- Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15] 

# import os
# import math


# os.system('clear')

# def ask_number_list():
#     str_list = input('Введите числа через пробел: ').split(' ')
#     number_list = []
#     for val in str_list:
#         if(val.isdigit()):
#             number_list.append(int(val))
#     return number_list

# def mult_pairs(list_numbers):
#     mult_list = []
#     length = len(list_numbers)
#     for i in range(math.ceil(length/2)):
#         mult_list.append(list_numbers[i]*list_numbers[length-i-1])
#     return mult_list

# num = ask_number_list()
# print(f'{num} => {mult_pairs(num)}')




# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. 
# Пример:  [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

# import os


# os.system('clear')

# def ask_number_list():
#     str_list = input('Введите числа через пробел: ').split(' ')
#     number_list = []
#     for val in str_list:
#         if(isfloat(val)):
#             number_list.append(float(val))
#     return number_list

# def isfloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False

# def max_min_dif(numbers):
#     new_list = []
#     for n in numbers:
#         new_list.append(n - int(n))
#     max = new_list[0]
#     min = new_list[0]
#     for i in range(1,len(new_list)):
#         if(new_list[i] > max):
#             max = new_list[i]
#         if(new_list[i] < min):
#             min = new_list[i]
#     return round(max - min, 3)

# def get_afterpoint(fnum):
#     strnum = str(fnum)
#     return int(strnum[strnum.index('.')+1:])

# nums = ask_number_list()
# dif = max_min_dif(nums)
# print(f'{nums} => {dif} или {get_afterpoint(dif)}')


# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

# import os


# os.system('clear')

# def ask_number():
#     number = input(f'Введите число: ')
#     if(not number.lstrip('+ -').isdigit()):
#         print('Ошибка: вы ввели не число! Повторите ввод')
#         return ask_number()
#     return int(number)

# def to_binary(number):
#     result = ''
#     while(number != 0):
#         result += str(number%2)
#         number = int(number/2)
#     return result[::-1]

# num = ask_number()
# print(f'{num} -> {to_binary(num)}')


# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import os

# очищаем консоль
os.system('clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

def negafib(number):
    ls = []
    if (number < 0):
        number = -number

    # negativ
    prev = 0
    next = 1
    ls.append(prev)
    ls.append(next)
    for i in range(1, number):
        sum = prev - next
        prev = next
        next = sum
        ls.append(sum)
    ls.reverse()

    # positiv
    prev = 0
    next = 1
    ls.append(next)
    for i in range(1, number):
        sum = prev + next
        prev = next
        next = sum
        ls.append(sum)
    return ls

num = ask_number()
print(negafib(num))

