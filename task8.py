# Task 1
# Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. 
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

text = input('Enter numbers:')

def arithmetic(sequence):
    numbers = [int(x) for x in sequence.split(',')]
    difference = numbers[1] - numbers[0]
    next_term = numbers[-1] + difference
    return next_term

def geometric(sequence):
    numbers = [int(x) for x in sequence.split(',')]
    ratio = numbers[1] / numbers[0]
    next_term = numbers[-1] * ratio
    return next_term

def square(sequence):
    numbers = [int(x) for x in sequence.split(',')]
    next_term = (len(numbers) + 1) ** 2
    return next_term

def cube(sequence):
    numbers = [int(x) for x in sequence.split(',')]
    next_term = (len(numbers) + 1) ** 3
    return next_term

res = arithmetic(text)
print(f'Next number in arithmetic sequence: {res}')

res = geometric(text)
print(f'Next number in geometric sequence: {res}')

res = square(text)
print(f'Next number in square sequence: {res}')

res = cube(text)
print(f'Next number in cube sequence: {res}')

# OR

def parse_text(text: str) -> list:
    """

    :param text:
    :return:
    """
    punctuations = ',:;'
    for char in punctuations:
        text = text.replace(char, ' ')
    return list(map(int, text.split()))


def is_arithmetic(numbers: list) -> bool:
    """

    :param numbers:
    :return:
    """
    if len(numbers) < 3:
        return False
    d = numbers[1] - numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != d:
            return False
    return True


def is_geometric(numbers: list) -> bool:
    """

    :param numbers:
    :return:
    """
    if len(numbers) < 3:
        return False
    q = numbers[1] // numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i + 1] // numbers[i] != q:
            return False
    return True


def next_arithmetic_item(numbers: list) -> int | float:
    """

    :param numbers:
    :return:
    """
    if len(numbers) < 3:
        return None
    d = numbers[1] - numbers[0]
    return numbers[-1] + d


def next_geometric_item(numbers: list) -> int | float:
    """

    :param numbers:
    :return:
    """
    if len(numbers) < 3:
        return None
    q = numbers[1] // numbers[0]
    return numbers[-1] * q


def next_sequence_item(numbers: list) -> int | float:
    """

    :param numbers:
    :return:
    """
    if is_arithmetic(numbers):
        return next_arithmetic_item(numbers)
    if is_geometric(numbers):
        return next_geometric_item(numbers)
    return None


def main():
    """
    
    :return: 
    """
    text = input('numbers>>')
    numbers = parse_text(text)
    item = next_sequence_item(numbers)
    print(f'Next item is {item}')


if __name__ == '__main__':
    main()

# Task 2
# Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99. 
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, множенням яких чисел він є.

max_palindrome = max(
    (i * j, (i, j))
    for i in range(100, 1000)
    for j in range(i, 1000)
    if str(i * j) == str(i * j)[::-1]
)

result, factors = max_palindrome

print(f'Largest palindrome: {max_palindrome}')

# OR

def is_palindrome(item: int) -> bool:
    """
    
    :param item: 
    :return: 
    """
    item = str(item)
    return item == item[::-1]


def max_palindrome(start: int, stop: int) -> int:
    """
    
    :param start: 
    :param stop: 
    :return: 
    """
    if stop < start:
        start, stop = stop, start

    result = []
    for i in range(start, stop):
        for j in range(start, stop):
            if is_palindrome(i * j):
                result.append((i, j, i * j))

    return max(result, key=lambda item: item[2])


def main():
    print(max_palindrome(100, 1000))


if __name__ == '__main__':
    main()