# 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр. Учтите, что числа могут быть отрицательными.

# number = input('Введите вещественное число: ')
# def sum_in_number(s_number):
#     sum = 0
#     for i in s_number:
#         if i.isdigit():
#             i = int(i)
#             sum = sum + i
#     print(sum)
# sum_in_number(number)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# number = int(input('введите число N: '))
# count = 1
# sum = 1
# while count <= number:
#     for i in range(1,number+1):
#         sum = sum*i
#         print(sum)
#         count += 1

# 3. Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# import random
# num = int(input("Введите число массива: "))
# numbers = []   
# for i in range(num):
#     numbers.append(random.randint(-9,10))
# print(f"Полученный рандомный массив: {numbers}")
# i = 0
# for n in numbers:
#     i += 1
#     if n < 0:
#         numbers.insert(i, 0)
# print(f"Обновленный массив с нулями: {numbers}")

# 4. Составьте алгоритм нахождения случайного числа без использования библиотеки random.

# import datetime 

# min_n = 10
# max_n = 100

# def get_rand():
#     return datetime.datetime.now().microsecond%100

# n = get_rand()

# print(n)