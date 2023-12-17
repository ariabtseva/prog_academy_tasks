# # Task 1
# # Напишіть скрипт, який порахує скільки літер «b» у введеному рядку тексту.

# b = input('text = ').lower().count('b')
# print(f'b = {b}')

# # Task 2
# # Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного 
# # ім'я на валідність (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно 
# # починатися з великої літери, за якою повинні йти маленькі).

# name = input('name:')
# if len(name) >= 2 and name.replace(' ', '').isalpha() and name.istitle():
# # if not name[0].isupper() or not all(char.islower() for char in name[1:]) and any(char.isdigit() for char in name):
#     print('name invalid')
# else:
#     print('name valid')

# # Task 3
# # Напишіть скрипт, який обчислює суму всіх кодів символів рядка.

# text = input('text = ')
# res = sum(map(ord, text))
# print(res)
# # ascii = 0

# # for char in text:
# #     ascii += ord(char)

# # print(f'ascii sum: {ascii}')

# # Task 4
# # Виведіть на екран 10 рядків із значенням числа Pi. 
# # У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.

# import math

# for i in range(2, 12):
#     # p = round(math.pi, i)
#     print(f'{math.pi:.{i}f}')

# # Task 5
# # Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.

# text = input('text = ').split
# print(max(text, key=len))
# # max_w = max(len(word) for word in words)
# # longest_w = [word for word in words if len(word) == max_w]
# # print(longest_w)

# Task 6
# Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери). 
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. Напишіть програму, 
# яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"

text = input('text = ')
for i in range(1, len(text) + 1):
    pattern = text[:1]
    print(pattern)
    if len(pattern) * text.count(pattern) == len(text):
        print(pattern)
        break
else:
    print('Syntax error')

# Task 7
# Напишіть скрипт для очищення тексту від HTML-тегів.
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
# - тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">

html = ''

while '<' in html:
    l_index = html.find('<')
    r_index = html.find('>')
    html = html.replace(html[l_index: r_index + 1], '')

print (html)