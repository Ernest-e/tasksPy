#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%% 
"""
Треугольник существует только тогда, 
когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
то треугольника с такими сторонами не существует. 
Отдельно сообщить является ли треугольник разносторонним, 
равнобедренным или равносторонним.
"""

a = int(input('enter A length: '))
b = int(input('enter B length: '))
c = int(input('enter C length: '))


if (a > (b+c)) or (b > (a+c)) or (c > (a+b)):
    print ('Triangle doesnt exist')
elif a == b == c:
    print('Triangle is equilateral')
elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
    print('Triangle is isosceles')
else:
    print ('Triangle is scalene')

    

#%% 
"""
Напишите код, который запрашивает число и сообщает 
является ли оно простым или составным. 
Используйте правило для проверки: 
“Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

a = int(input('Enter a positive number less then 100_000: '))

def isPrime(n):
    if n == 0:
        return True
    if n % 2 == 0:
        return True
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

if a < 0 or a > 100_000:
    print('Error')
elif isPrime(a):
    print('number is prime')
else:
    print('number is composite')
    
    
#%%
"""
Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
"""

from random import randint

num = randint(0, 1000)

trial = 0

while trial < 10:
    a = int(input('enter a number: '))
    if a == num:
        print('you win')
        break
    
    trial += 1

    
if trial == 10: 
    print('you lose, hidden number is ', num)
    

    
    