"""
Exercise 1
Yechezkel Chen 325191419
"""


# Task 1.1
def getPentaNum(n):
    return n * (3 * n - 1) / 2


# Task 1.2
def pentaNumRange(n1, n2):
    return (getPentaNum(i) for i in range(n1, n2))


# Task 2
def sumDigit(n):
    return sum(int(digit) for digit in str(n))


# Task 3
gematria = {
    'א': 1,
    'ב': 2,
    'ג': 3,
    'ד': 4,
    'ה': 5,
    'ו': 6,
    'ז': 7,
    'ח': 8,
    'ט': 9,
    'י': 10,
    'כ': 20,
    'ל': 30,
    'מ': 40,
    'נ': 50,
    'ס': 60,
    'ע': 70,
    'פ': 80,
    'צ': 90,
    'ק': 100,
    'ר': 200,
    'ש': 300,
    'ת': 400
}


def gematriaValue(str):
    return sum(gematria[char] for char in str)


# Task 4.1
def isPrime(n, divisior=2):
    if n <= 1:
        return False
    if n == divisior:
        return True
    if n % divisior == 0:
        return False
    if divisior * divisior > n:
        return True
    return isPrime(n, divisior + 1)


# Task 4.2
def getTwin(n):
    if isPrime(n + 2):
        return n + 2
    elif isPrime(n - 2):
        return n - 2
    else:
        return None


# Task 4.3
def getTwinDicationry(n):
    prime_nums = tuple(filter(lambda x: isPrime(x), range(1, n + 1)))
    return dict(zip(prime_nums, map(lambda x: getTwin(x), prime_nums)))


# Task 5
'''
d1 = {'a': [1, 2], 'b': [3,4]}
d2 = {'b': [3], 'c': [4, 5]}
d3 = {'a': [2, 3], 'd': [5, 6]}
'''
from collections import defaultdict


def add3dicts(d1, d2, d3):
    result_dict = defaultdict(tuple)

    for d in (d1, d2, d3):
        for key, value in d.items():
            result_dict[key] = tuple(set(result_dict[key]) | set(value))

    return dict(result_dict)


# Task 6.1
def multiBy2(x):
    return x * 2


def square(x):
    return x * x


def inverse(x):
    return 1 / x


functions = [multiBy2, square, inverse]


# Task 6.2
def dictFunctions(nums, functions):
    new_nums = tuple(map(lambda func: tuple(map(lambda x: func(x), nums)), functions))
    return dict(zip(map(lambda func: func.__name__, functions), new_nums))
