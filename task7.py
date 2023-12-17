# Task 1
# Напишіть програму, яка перевіряє, чи всі елементи в списку є унікальними.

def are_unique(input_list):
    return len(input_list) == len(set(input_list))

text = list(input('Enter:').split())

print('All elements are unique' if are_unique(text) else 'Duplicated elements')

# or

import random
x = [random.randint(1, 100) for _ in range(10)]

res = 'Yes' if len(set(x)) == len(x) else 'No'
print(x)
print(res)

# Task 2
# Напишіть програму, яка приймає список елементів і повертає кількість унікальних елементів.

def count_unique(input_list):
    return len(set(input_list))

text = list(input('Enter:').split())
res = count_unique(text)

print(res) 

#or

import random
x = [random.randint(1, 100) for _ in range(10)]

res = 'Yes' if len(set(x)) == len(x) else 'No unique elements'
print(x)
print(res)

# Task 3
# Напишіть програму, яка приймає словник і перевіряє, чи містяться в ньому унікальні значення.

import random

x = {i: random.randint(1, 10) for i in range(10)}

res = 'Yes' if len(x) == len(set(x.values())) else 'No'
print(x)
print(res)

# Task 4
# Припустимо, що у тебе є дані про дружбу між користувачами соціальної мережі:
# friendships = {
#     "user1": {"user2", "user3", "user4"},
#     "user2": {"user1", "user3"},
#     "user3": {"user1", "user2", "user4"},
#     "user4": {"user1", "user3"}
# }
# Напишіть програму для розрахунку спільних друзів у соціальній мережі, імена яких задає користувач.

friendships = {
     "user1": {"user2", "user3", "user4"},
     "user2": {"user1", "user3"},
     "user3": {"user1", "user2", "user4"},
     "user4": {"user1", "user3"}
}

user_1, user_2 = input('username:').lower().strip(),\
                 input('username:').lower().strip()

mutual = friendships.get(user_1, set()) & friendships.get(user_2, set())
print(mutual)

# Task 5
# Напишіть програму, яка повертає найдовше слово, яке міститься одночасно у двох рядках.

text_1 = input('text = ').lower().split()
text_2 = input('text = ').lower().split()

res = set(text_1) & set(text_2)
print(max(res, key=len))

# Task 1
# Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.

def func(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return f'{a + b}{c}'


print(func(1, 2, 'sss'))

# Task 2
# Реалізуйте функцію, яка малює на екрані прямокутник із зірочок 
# «*». Її параметрами будуть цілі числа, які описують довжину та 
# ширину такого прямокутника.

def rectangle(height, width):
    res = f"{'*' * width}\n" +\
          f"*{' ' * (width - 2)}*\n" * (height - 2) +\
          f"{'*' * width}\n"
    return res

print(rectangle(5, 6))
f = open('test.txt', 'w')
print(rectangle(5, 6), file=f)

# Task 3
# Напишіть функцію, яка реалізує лінійний пошук елемента у списку
#  цілих чисел. Якщо такий елемент у списку є, то поверніть індекс, 
# якщо ні, то поверніть число «-1».

def linear_search(seq, x):
    for index, item in enumerate(seq):
        if item == x:
            return index

    return -1
 
def linear_search_all(seq, x):
    indexes = []
    for index, item in enumerate(seq):
        if item == x:
            indexes.append(index)

    return indexes

# Task 4
# Напишіть функцію, яка поверне кількість слів у текстовому рядку.

def num_words(text):
    return len(text.split())

# Task 5
# Напишіть функцію, яка переводить число, що означає кількість 
# доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

import num2words
money = input('$=')
dollars, cents = money.split('.')
dollars = num2words.num2words(dollars)
cents = num2words.num2words(cents)
res = f'{dollars} dollars {cents} cents'
print(res)