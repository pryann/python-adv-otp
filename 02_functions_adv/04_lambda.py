def increase_by_one(value):
    return value + 1


# increase_by_one = lambda value: value + 1


def apply(numbers, fn):
    result = []
    for number in numbers:
        atomic_result = fn(number)
        result.append(atomic_result)
    return result


print(apply([1, 2, 3], lambda x: x * 2))

# anonim IIFE - Imediately Invoked Function Expression
print((lambda num: num + 1)(10))


def make_incrementor(n):
    return lambda x: x + n


f_42 = make_incrementor(42)
print(f_42(10))

print(make_incrementor(42)(10))
