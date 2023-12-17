# t = int(input('t='))
# money = int(input('das geld='))

# if t < 10 and money >= 1000 or t >= 10:
#     print('Time for a walk')
# else:
#     print('Stay at home bozo')
# print('Have a nice life')

# if t > 20:
#     print('Summer')
# elif t > 5:
#     print('Autumn or Spring')
# else:
#     print('Winter')

# p = int(input('point='))
# if p < 0 or p >= 100:
#     print('Error')
# elif p > 89:
#     print('A')
# elif p > 69:
#     print('B')
# else:
#     print('F')

# x = int(input('x='))
# res = 'Odd' if x % 2 else 'Even'
# print(res)

# def f(start, stop, step):
#     start = start or 0
#     stop = stop or 0
#     step = step or 0
#     return start, stop, step
# print(f(None, 55 , None))

# text = input('text')
# if text:
#     print(text.upper())
# else:
#     print('Empty')

# text = input('text')
# if not text:
#     print('Empty')

# x = list('Hello')
# x = set('Hello')
# print(x)

# x = [1, 2, 4]
# y = []
# z = list('Hello')
# res = x + z #Copy of 2 lists
# print(res)
# res1 = 1 in x

# import copy
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# y = copy.deepcopy(x)
# y[0][0] = 100
# print(y)
# print(x)

# a = [1, 2, 3, 4, 4, 4]
# print(a.count(4))

# a = [1, 2, 3, 4, 4, 4]
# import random
# a = []
# for i in range(10):
#     a.append(random.randint(100, 1000))
# print(a) #Not the Python way

# a = [100, 1, 2, 3, 4, 4, 4]
# a.reverse()
# print (a)
#or
# b = a[::-1]
# print(a)
# print(b)
#or
# for item in reversed(a):
#     print(item)

# print(a.index(4))

# a.sort(reverse=True)
# print(a)

# b = sorted(a, reverse=True)
# print(b)

# a = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [10, 20, 30, 40]

# x = a.pop(-2)
# print(a)
# print(x)
# x = a.pop(-2)
# print(a)
# print(x)

# x = a.clear()
# del a # Delete link

# a.insert(2, 10000)
# print(a)

# a.extend(b) # doesnt create new list
# print(a)

# m = 1
# if m in (1, 3, 5, 7, 9):
#     print(31)

# i = 1
# while i <= 5:
#     if i == 2:
#         i += 1
#         continue
#     print(1)
#     i += 1
# else:
#     print('End')

# i = 1
# x = []
# while i <= 5:
#     ans = int(input('number = '))
#     if ans == 0:
#         break
#     x.append(ans)
#     i = 1
# else:
#     print(x)

# n = int(input('number = '))
# i = 2
# while i < n:
#     if n % i == 0:
#         print('not prime')
#         break
#     i += 1
# else:
#     print('prime')

# while True:
#     n = int(input('n = '))
#     if n > 0:
#         break
#     print('Error')

# x = [1, 2, 3, 4, 5]
# for item in x:
#     print(item)

# x = [1, 2, 3, 4, 5]

# i = 0
# while i < len(x):
#     x[i] += 10
#     i += 1
# print(x)
# OR (better)
# for i in range(len(x)):
#     x[i] += 10
# print(x)
# OR !!!!!!! (the best)
# for index, item in enumerate(x):
#     x[index] = item + 10
# print(x)

# import random
# x = []
# for _ in range(10):
#     x.append(random.randint(1, 10))
# print(x)
# or
# x = [random.randint(1, 10) for _ in range(10)]
# print(x)

# x = [2, 3, 4, 2, 3, 5, 6, 6, 9]
# y = [item + 10 for item in x if item % 2]
# print(y) 

# z = 'Hello'
# y = [f'*{item}*' for item in z]
# print(y) 

# x = ['2', '3', '4', '2', '3', '5', '6', '6', '9']
# # for index, item in enumerate(x):
# #     x[index] = int(item)
# # print(sum(x))
# # and
# x = list(map(int, x))
# print(x)

# x = [2, 3, 4, 5, 6, 7]
# y = ['fail', 'sat', 'good', 'exl']
# # res = list(zip(x, y))
# # print(res)
# # or
# for item_x, item_y in zip(x, y):
#     print(item_x, item_y)

# res = []
# while True:
#     x = int(input('number = '))
#     if x == 0:
#         break
#     res.append(x)
# print(res)
# or
# res = []
# while (x := int(input('number = '))) != 0:
#     res.append(x)
# print(res)

# for i in range(256):
#     print(i, chr(i))
# print(ord('Ї'))

# x = 'Hello'
# y = 'y'
# print(x > y)

# x = 'Hello'
# # x = 10 * x
# # print(x)
# print('ll' in x)
# print('LL' in x)
# print('LL' not in x)
# print(x[0])

# x = 'Hello'
# y = 'asdasd'
# res = x + y
# print(res)

# x = 'Hellolluu '
# y = x.replace('ll', '*')
# print(y)

# text = input('text = ')
# while '  ' in text:
#     text = text.replace('  ', ' ')
# print(text)

# text = input('text = ')
# text = text.split()
# text2 = text.split(' ')
# print(text)
# print(text2)

# s = ['1', '2', '3', '4']
# # # DO NOT 
# # for item in s:
# #     res += item
# # print(res)
# # DO
# y = '*'.join(s)
# y = ''.join(s)
# print(y)

# text = input('text = ')
# text = text.split()
# text = ' '.join(text)
# print(text)

# x = [
#     '1 Bob Simson 19.58$ decorations',
#     '2 Mary 66.7$ food',
#     '3 Mary 98.91$ toys',
#     '4 Aleksa 72.29$ drinks',
# ]
# s = 0
# for line in x:
#     res = line.split()
#     money = res[-2]
#     s += float(money.replace('$', ''))
# print(f'{s}$')

# import string
# text = input('text = ')
# for item in string.punctuation:
#     text = text.replace(item, ' ')
# print(text.split())

# import string
# text = input('text = ')
# for item in string.punctuation:
#     text = text.replace(item, ' ')
# words = text.split()
# for word in words:
#     if words.count(word):
#         print(word)
# #or
# print(set(words)) #no duplicates

# days = {
#     1: 'one', 2: 2, 'three': '3', 4: ('4', 'four'), ('5', 'five'): 'Пять'
# }
# # # for item in days:
# # #     print(item, days[item])
# # days[1] = 'one'
# # days[10] = 'десять'
# # # print(days.keys())
# # # print(days.values())
# # # print(days.items())
# # for key, value in days.items():
# #     print(f'{key}; {value}')

# a = dict(one=1, two=2, three=3)
# print(a)

# a = dict((('one', 1), ('two', 2), ('three', 3)))
# print(a)

# x = [1, 2, 3]
# y = ['one', 'two', 'three']
# a = dict(zip(x, y))
# b = dict(zip(y, x))
# print(a)
# print(b)

# if 0 in days:    
#     print(days[0])
#or 
# res = days.get(0, 'Error')
# print(res)

# calc = {
#     '+': operator.add,
#     '-': operator.add,
#     '*': operator.mul,
#     '/': operator.truediv,
# }
# a, b = int(input('a = ')), int(input('b = '))
# operation = input('operation is ')
# res = calc.get(operation)
# res = res(a, b) if res else 'Error'
# print(res)

# address = {
#     'city': 'Kyiv',
#     'street_home': {
#         'street': 'Peremohy',
#         'ap': '123'
#     }
# }
# print(address['city'])
# print(address['street_home']['street'])

# names = ['Ivan1', 'Ivan2', 'Ivan3']
# age = 25
# users = {name: age for name in names}
# print(users)

# days = {
#     1: 'monday', 
#     2: 'tuesday', 
#     3: 'wednesday', 
#     4: 'thursday', 
#     5: 'friday', 
#     6: 'saturday', 
#     0: 'sunday'
# }
# day = int(input('day = '))
# print(days.get(day % 7))

# text = input('text = ')
# res = {}
# for char in text:
#     if char in res:
#         res[char] += 1
#     else:
#         res[char] = 1
# print(res)
# __________
# text = input('text = ')
# res = {}
# for char in text:
#     if char not in res:
#         res[char] = text.count(char)
# print(res)

# x = set('Hello')
# print(x)
# x = {1, 2, 3, 4, 5, 'Hello'} #no {inside {}}
# print(x)

# text = input('text = ')
# res = {}
# for char in set(text):
#     res[char] = text.count(char)
# print(res)

# text_1 = input('text = ').lower().split()
# text_2 = input('text = ').lower().split()
# print(set(text_1) | set(text_2))

# def add(a, b):
#     return a + b
# print(add(1, 2))
# print(add('1', '2'))
# print(add(11, 2.3))

# def add(a, b, c=10):
#     return a + b + c
# print(add(1, 2, 3))

# def func(a, b=[]):
#     b.append(a)
#     return b
# print(func(12))
# print(func(13))
# print(func(14))
# OR
# def func(a, b=None):
#     if not b:
#         b = []
#     b.append(a)
#     return b
# print(func(12))
# print(func(13))
# print(func(14))

# n = 5
# for i in range(n):
#     n += 1
#     print(i)

# def add(a: int | float, b: int | float, c: int | float =10) -> int | float:
#     """
#     Returns sum of three numbers.
#     :param a: 3 salary
#     :param b: 9 salary
#     :param c: 12 salary
#     :return: avg salary
#     """
#     return a + b + c 
# print(add(1, c=2, b=3))
# print(add.__doc__)
# print(add('1', '2', '3'))

# def func(a, *args):
#     # for item in args:
#     #     #__
#     return args
# res = func(1, 2, 3, 4)
# print(res)

# def func(a, b, *args, d=5, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
#     print(b)
#     print(d)
# func(1, 2, 3, 4, 5, 6, d=7, c=8)
# # func(1)
# # func(1, 2)

# def calc(*args, operation='+'):
#     for item in args:
#         if not isinstance(item, int | float):
#             raise TypeError()
#     if operation == '+':
#         return sum(args)
#     if operation == '*':
#         res = 1
#         for item in args:
#             res *= item
#         return res
#     return None

# def text_to_numbers(text: str):
#     for char in ',;':
#         text = text.replace(char, ' ')
#     return list(map(int, text.split()))
# # def numbers_odd(numbers):
# #     result = []
# #     for item in numbers:
# #         if item % 2:
# #             result.append(item)
# #     return result
# # def numbers_positive(numbers):
# #     result = []
# #     for item in numbers:
# #         if item > 0:
# #             result.append(item)
# #     return result
# # ______OR______
# def is_odd(item):
#     return item % 2
# def is_positive(item):
#     return item > 0
# # text = input('numbers:')
# # numbers = text_to_numbers(text)
# #______OR______
# def filter(numbers, func):
#     result = []
#     for item in numbers:
#         if func(item):
#             result.append(item)
#     return result
# text = input('numbers>>')
# numbers = text_to_numbers(text)
# print(filter(numbers, is_odd))
# print(filter(numbers, is_positive))
# print(filter(numbers, lambda item: item % 2 == 0))
# print(filter(numbers, lambda item: item < 0))

# text = 'sadsfsmsaf ad fasdsa d asd sad asdasd'.split()
# print(max(text, key=lambda item: item.count('s')))

# text = {1: 100, 2: 2222, 3: 444, 5: 666}
# print(max(text, key=lambda key: text[key]))

# _____
# x = 5
# def func():
#     x = 3
#     def inner():
#         # global x
#         # nonlocal x
#         x = 4
#     inner()
#     print(x)
# func()
# f1()
# print(x)

# x = [5]
# def func(x):
#     x.append(3)
# func(x)
# print(x)

# # import functools
# # @functools.lru_cache
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(6))

# def print_numbers(i):
#     if i == 0:
#         return
#     print_numbers(i - 1)
#     print(i)
# print_numbers(10)

# def my_pow(a, b):
#     if b == 0:
#         return 1
#     return a * my_pow(a, b - 1)
# print(my_pow(2, 8))

# # open('test.txt', 'rb')
# f = open('test.txt', 'w', encoding='utf-8')
# x = [1, 2, 3, 4, 5, 6, 7]
# f.writelines(map(str, x))
# f.writelines(map(lambda item: f'{item}\n', x))
# # f.write('Oleh\n')
# # f.write('Python\n')
# # f.write('December\n')
# f.flush()
# f.close()

# with open('test.txt', 'w', encoding='utf-8') as file:
#     x = [1, 2, 3, 4, 5, 6, 7]
#     file.writelines(map(lambda item: f'{item}\n', x))

# with open('test.txt', 'r', encoding='utf-8') as file:
#     # # # data = file.read()
#     # # # print(data)
#     # # # or
#     # # while (data := file.read(3)):
#     # #     print(data)
#     # while data := file.readlines():
#     #     print(data.strip())
#     for line in file:
#         print(line.strip())

# import random
# with open('test.txt', 'w', encoding='utf-8') as file:
#     for i in range(1_000_000):
#         file.write(f'{random.randint(1, 1000)}\ns')

# import timeit
# stmt1 = """file = open('test.txt')
# s = 0
# data = file.readlines()
# for item in data:
#     if item.strip().isdigit():
#         s += int(item)
# print(s)
# file.close() """
# #or
# stmt2 = """file = open('test.txt')
# s = 0
# for item in file:
#     if item.strip().isdigit():
#         s += int(item)
# print(s)
# file.close()"""
# print(timeit.timeit(stmt1, number=10))
# print(timeit.timeit(stmt2, number=10))

