def increase_price_by_tax(tax_rate=0.27):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            value = fn(*args, **kwargs)
            increased_value = value * (1 + tax_rate)
            return round(increased_value, 2)

        return wrapper

    return decorator


def apply_discount(discount=0.05):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            value = fn(*args, **kwargs)
            discount_value = value * (1 - discount)
            return round(discount_value, 2)

        return wrapper

    return decorator


@apply_discount(0.1)
@increase_price_by_tax(0.27)
def summa(a, b):
    return a + b


print(summa(100, 200))
# print(increase_price_by_tax(0.27)(summa)(100, 200))
