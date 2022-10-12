#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#d =  int(input("Введите число для заданной точности числа Пи:\n"))
#print(f'число Пи с заданной точностью {d} равно {round(d, 10)}')

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#Пример:
#N = 20 => [2, 2, 5]

#num = int(input("Введите число: "))
#i = 2 # первое простое число
#lst = []
#old = num
#while i <= num:
#    if num % i == 0:
#        lst.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
#print(f"Простые множители числа {old} приведены в списке: {lst}")

#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#lst = list(map(int, input("Введите числа через пробел:\n").split()))
#print(f"Исходный список: {lst}")
#new_lst = []
#[new_lst.append(i) for i in lst if i not in new_lst]
#print(f"Список из неповторяющихся элементов: {new_lst}")

#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#from calendar import c
#import os
#os.system("cls")
#from random import randint
#import itertools

#k = int(input('Задайте натуральную степень k: '))

#ratio_list = list([randint(0, 101) for i in range(k+1)]) # задаем случайный список
#if ratio_list[0] == 0: # если будет равен 0, то многочлен может быть неверным
#    ratio_list[0] = randint(1, 100)
#print(ratio_list)

#def get_polynomial(k, ratio_list): 
#    str1 = ['*x**']*(k-1) + ['*x']
#    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    # с помощью этого метода мы объединяем несколько списков в список кортежей с самой длинной итерацией
    # пустые кортежи заполняем пустотой ('')
#    print(polynomial)
#    for x in polynomial:
#        x.append(' + ') # проставляем + между кортежами
#    polynomial = list(itertools.chain(*polynomial)) # объединяем в один список
#    print(polynomial)
#    polynomial[-1] = ' = 0' # добавляем концовочку (меняем последний '+' на '= 0')
#    return "".join(map(str, polynomial)).replace(' 1*x',' x') # возвращаем строку

#list = get_polynomial(k, ratio_list)
#print(list)

#with open('33_Polynomial.txt', 'w') as data:
#    data.write(list)
#with open('33_Polynomial2.txt', 'w') as data:
#    data.write(list)

#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
#Пример:
#файл1: 2x^2 + 7x + 5
#файл2: 4x^2 + 3x + 9
#результат: 6x^2 + 10x + 14


#with open('poly_1.txt', 'w', encoding='utf-8') as file:
#    file.write('2*x^2 + 7*x + 5')
#with open('poly_2.txt', 'w', encoding='utf-8') as file:
#    file.write('4*x^2 + 3*x + 9')

#with open('poly_1.txt','r') as file:
#   poly_1 = file.readline()
#    list_of_poly_1 = poly_1.split()


#with open('poly_2.txt','r') as file:
#   poly_2 = file.readline()
#    list_of_poly_2 = poly_2.split()

#print(f'{list_of_poly_1} + {list_of_poly_2}')
#sum_poly = list_of_poly_1 + list_of_poly_2

#with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#    file.write(f'{list_of_poly_1} + {list_of_poly_2}')

#    sum_of_poly = (list_of_poly_1), '+' (list_of_poly_2)

#    if len(poly_1) > len(poly_2):
#         help_poly = poly_1
#    poly_1 = poly_2
#    poly_2=help_poly
#poly_1 = poly_1.split(' + ')
#poly_2 = poly_2.split(' + ')
#print(poly_1,poly_2)

#count1 =0
#count2=len(poly_2)-len(poly_1)
#new_poly = ''
#for i in range(count2):
#     new_poly += poly_2[i] + '+'

#ind1 = ''
#ind2 = ''

#for i in range(len(poly_2) - len(poly_1), len(poly_2)):
#     result = 0 
#     if i == len(poly_2) - 1:
#         result += int(poly_1[-1][:-4]+poly_2[-1][:-4])
#         new_poly += str(result) + poly_1[-1][-4:]
#     elif i == len(poly_2) - 2:
#         result += int(poly_1[-2][:-2]+poly_2[-2][:-2])
#         new_poly += str(result) + poly_1[-2][-2:] + ' + ' 
#     else:
#         result += int(poly_1[count1][:-4]+poly_2[count2][:-4])
#         new_poly += str(result) + poly_1[count1][-4:] + ' + ' 
#         count1 += 1
#         count2 += 2
#print(new_poly)