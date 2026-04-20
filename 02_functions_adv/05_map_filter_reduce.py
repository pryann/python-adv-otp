from functools import reduce
from random import randint

from numpy import number


numbers = [1, 2, 3, 4, 5, 6]


# def duplicate_value(values):
#     result = []
#     for value in values:
#         result.append(value * 2)
#     return result


# doubled_numbers = duplicate_value(numbers)

# list comprehension
doubled_numbers = [number * 2 for number in numbers]

# map function: functional programming
doubled_numbers = list(map(lambda x: x * 2, numbers))
# print(type(doubled_numbers))


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]

summa = reduce(lambda a, b: a + b, numbers)
print(summa)

numbers = [randint(1, 10_000) for i in range(100)]

# fmt: off
value = reduce(lambda x, y: x + y, 
              map(lambda x: x**2, 
                  filter(lambda x: x > 5000, numbers)))

value = sum([x**2 for x in numbers if x > 5000])
