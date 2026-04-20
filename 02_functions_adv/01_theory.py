# assign to a variable
def log_error(message):
    print(f"ERROR: {message}")


log = log_error
log("An error message")


# embed to an another function
# non a real app like usage, just for demonstration
def outer_function(text):
    msg = text.upper()

    def inner_function():
        print(msg)

    inner_function()


outer_function("Mizu")


# closure, hof, scope
def make_incrementor(n):
    def incrementor(x=1):
        return x + n

    return incrementor


inc = make_incrementor(10)
print(inc())
print(inc(10))
# print(make_incrementor(10)(2))


# callback
def aritmentic_operation(x, y, operation_fn):
    return operation_fn(x, y)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


print(aritmentic_operation(10, 5, add))
print(aritmentic_operation(10, 5, subtract))


def openForWrite():
    def inner_open():
        return open(
            file="file.txt",
            mode="w",
            encoding="utf-8",
        )

    return inner_open


with open(
    file="file.txt",
    mode="r",
    encoding="utf-8",
) as f:
    pass
