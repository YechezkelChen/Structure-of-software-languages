"""
Exercise 2
Yechezkel Chen 325191419
"""

from datetime import datetime, timedelta
from functools import reduce

# Task 1
y = lambda x: x / 2 + 2

# Task 1.1
y_values = list(map(y, list(range(10001))))

# Task 1.2
sum_of_y_values = reduce(lambda t, s: s + t, y_values)

# Task 1.3
# super function
start1 = datetime.now()
super_func = reduce(lambda t, s: s + t, y_values)
total1 = datetime.now() - start1

# imperative function
start2 = datetime.now()
count = 0.0
for value in y_values:
    count += value
total2 = datetime.now() - start2

# Task 1.4
result = reduce(lambda t, s: s + t, [y(x) for x in range(10001)])


# Task 2
lst = list(range(1, 1001))
even = list(filter(lambda x: x % 2 == 0, lst))
odd = list(filter(lambda x: x % 2 != 0, lst))

# Task 2.1
evanLambda = lambda x: reduce(lambda s, t: s * t, even[:(x // 2) + 1])
oddLambda = lambda x: y(sum(odd[:(x // 2) + 1])) + odd[(x // 2) + 1]

# Task 2.2
new_even = map(evanLambda, even[:-1])
new_odd = map(oddLambda, odd[:-1])

# Task 2.3
even_sum = reduce(lambda s, t: s + t, new_even)
odd_sum = reduce(lambda s, t: s + t, new_odd)


# Task 3
def generate_dates(start_date, amount, gap):
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    return list(map(lambda x: (start_date + timedelta(days=x * gap)).strftime("%d/%m/%Y"), range(amount)))


# Task 4.1
def power_function(exponent):
    return lambda x: pow(x, exponent)


# Task 4.2
def pow_map(n):
    return map(power_function, range(n))


# Task 4.3
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)


def taylor(n, x):
    power_functions = list(pow_map(n))
    return sum(map(lambda i: power_functions[i](x) / factorial(i), range(n)))


# Task 5
def task_manager():
    dic = {}

    def add_task(task, status="incomplete"):
        dic[task] = status

    def get_tasks():
        return dic

    def complete_task(task):
        dic[task] = "complete"

    return {'add_task': add_task, 'get_tasks': get_tasks, 'complete_task': complete_task}
