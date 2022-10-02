# ДЗ2
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

#x = input('Введите число ')

#def summa(x):                            
#    if float(x) < 0:                            
#        x = float(x) * (-1)
#    number = 0#
#    for i in str(x):
#        if i != '.':
#            number += int(i)
#    return number
#print(f'Сумма чисел равна {summa(x)}')

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#n = int(input('input N: '))
#factorial = 1
#for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

#from msilib import sequence
#n = int(input('Введите число: ')) 
#def get_squerence(n):
#    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
#nums = get_squerence(n)
#print(nums)
#print(round(sum(nums), 5))

#Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#from random import randint
#numbers = []
#for i in range(10):
#    numbers.append(randint (-10,10))
#print(numbers)
#
#def get_numbers(numbers):
#    count =0 
#    for element in numbers:
#        count +=1
#    return count
#print('Number of elements: ', get_numbers(numbers))
#
#x = int(input('Enter  position of first element: '))
#y = int(input('Enter position of second element: '))
#
#for i in range(len(numbers)):
#    mult = numbers[x -1]*numbers[y - 1]
#print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

#Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

#from random import Random, randint
#N = int(input('Введите число '))
#numbers = []
#for i in range(N):
#    numbers.append(randint(-N,N+1))
#print(numbers)
#
#def smes(numbers):
#    list = numbers[:]
#    numbers_length = len(list)
#    for i in range(numbers_length):
#        index = randint(0, numbers_length - 1)
#        temp = list[i]
#        list[i] = list[index]
##        list[index] = temp
#    return list
#print(smes(numbers))