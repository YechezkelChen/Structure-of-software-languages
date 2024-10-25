"""
Exercise 3
Yechezkel Chen 325191419
"""


# task 1
# regular recursion
def tuple_1000():
    def create_tuple(num):
        if num == 1:
            return (1,)
        return create_tuple(num - 1) + (num,)

    return create_tuple(1000)


# tail recursion
def tail_tuple_1000():
    def create_tuple(end, t=()):
        if end == 0:
            return t
        return create_tuple(end - 1, (end,) + t)

    return create_tuple(1000)


t = tail_tuple_1000()


# task 2
# regular recursion
def sum(t):
    if len(t) == 0:
        return 0
    return t[0] + sum(t[1:])


t_sum = sum(t)


# tail recursion
def tail_sum(t, sum=0):
    if len(t) == 0:
        return sum
    return tail_sum(t[1:], t[0] + sum)


t_sum = tail_sum(t)


# task 3
# regular recursion
def gcd(a, b):
    if b == 0:
        return a
    return a != 0 and gcd(b, a % b)


def lcm(a, b):
    gcd1 = gcd(a, b)
    if not gcd1:
        return 0
    return (a * b) / gcd1


# tail recursion
def tail_gcd(a, b):
    if b == 0:
        return a
    return tail_gcd(b, a % b)


def tail_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) / tail_gcd(a, b)


# task 4
# regular recursion
def is_palindrome(n):
    s = list(str(n))

    def is_palindrom(s):
        if len(s) == 0 or len(s) == 1:
            return True
        return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_palindrom(s)


# tail recursion
def tail_is_palindrome(n):
    s = list(str(n))

    def tail_is_palindrom(s):
        if len(s) == 0 or len(s) == 1:
            return True
        if s[0] != s[-1]:
            return False
        return is_palindrome(s[1:-1])

    return tail_is_palindrom(s)


# task 5
# regular recursion
def sorted_zip(lists):
    new_lists = sorted_lists(lists)
    return zip(*new_lists)


def sorted_lists(lists):
    if len(lists) == 0:
        return sorted(lists)

    rest_lists = sorted_lists(lists[:-1])
    rest_lists.append(sorted(lists[-1]))

    return rest_lists


# tail recursion
def sorted_zip(lists):
    new_lists = sorted_lists(lists)
    return zip(*new_lists)


def sorted_lists(lists, slists=[]):
    if len(lists) == 0:
        return slists
    return sorted_lists(lists[1:], slists + [sorted(lists[0])])


'''
Lazy Evaluation, Generators
'''

# task 1.1
import time
import sys


# without Lazy evaluation
def array_without_lazy_evaluation():
    start_time = time.time()
    array = list(range(10001))
    end_time = time.time()

    size_in_memory = sys.getsizeof(array)

    return array, end_time - start_time, size_in_memory


nonLazy_array, nonLazy_time, nonLazy_size = array_without_lazy_evaluation()


# with Lazy evaluation
def array_with_lazy_evaluation():
    start_time = time.time()
    array = range(10001)
    end_time = time.time()

    size_in_memory = sys.getsizeof(array)

    return array, end_time - start_time, size_in_memory


lazy_array, lazy_time, lazy_size = array_with_lazy_evaluation()


# task 1.2
# without Lazy evaluation
def slice_without_lazy_evaluation():
    start_time = time.time()
    sliced_array = nonLazy_array[:5000]
    end_time = time.time()

    size_in_memory = sys.getsizeof(sliced_array)

    return sliced_array, end_time - start_time, size_in_memory


nonLazy_slice_array, nonLazy_slice_time, nonLazy_slice_size = slice_without_lazy_evaluation()


# with Lazy evaluation
def slice_with_lazy_evaluation():
    start_time = time.time()
    sliced_array = lazy_array[:5000]
    end_time = time.time()

    size_in_memory = sys.getsizeof(sliced_array)

    return sliced_array, end_time - start_time, size_in_memory


lazy_slice_array, lazy_slice_time, lazy_slice_size = slice_with_lazy_evaluation()

print(type(nonLazy_array) == type(nonLazy_slice_array))
print(type(lazy_array) == type(lazy_slice_array))


# task 2
def is_prime(n, divisior=2):
    if n <= 1:
        return False
    if n == divisior:
        return True
    if n % divisior == 0:
        return False
    if divisior * divisior > n:
        return True
    return is_prime(n, divisior + 1)


def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# task 3
def taylor_series_e_to_x(x):
    term = 1.0
    total = term
    n = 1

    yield total

    while True:
        term *= x / n
        total += term
        n += 1
        yield total
