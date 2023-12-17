#Task 10.1

from collections import Counter
import re

def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r', encoding='utf-8') as file:
        words = re.findall(r'\b\w+\b', file.read().lower())
    return [word for word, _ in Counter(words).most_common(number_of_words)]

res = most_common_words('D:/111/lorem_ipsum.txt')
print(res)

# Task 10.2

import csv

def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        students = [{'name': name.strip(), 'average_mark': float(mark)} for name, _, mark in reader]

    top_performers = [student['name'] for student in sorted(students, key=lambda x: x['average_mark'], reverse=True)[:number_of_top_students]]
    return top_performers

res = get_top_performers('D:/111/students.csv')
print(res)