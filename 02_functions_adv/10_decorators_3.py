from time import perf_counter


def performance_meter(fn):
    def wrapper(name):
        start = perf_counter()
        fn(name)
        end = perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")

    return wrapper


@performance_meter
def say_hello(name):
    print(f"Hello {name}!")


say_hello("John")
