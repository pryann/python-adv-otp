from time import perf_counter


def performance_meter(fn):
    def wrapper():
        start = perf_counter()
        fn()
        end = perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")

    return wrapper


def say_hello():
    print("hello")


# perf = performance_meter(say_hello)
# perf()

performance_meter(say_hello)()
