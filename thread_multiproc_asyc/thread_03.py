from concurrent.futures import ThreadPoolExecutor
from time import ctime, sleep, time


def log_service(thread_name, delay):
    while logging:
        sleep(delay)
        print(f"{thread_name}: {ctime(time())}")


if __name__ == "__main__":
    max_tasks = 5
    logging = True
    with ThreadPoolExecutor(max_workers=max_tasks) as executor:
        # ('Thread-1', 1), ('Thread-2', 2), ('Thread-3', 3), ('Thread-4', 4), ('Thread-5', 5)
        args = ((f"Thread-{i}", i + 1) for i in range(max_tasks))
        # *args: [('Thread-1', 1), ('Thread-2', 2), ('Thread-3', 3), ('Thread-4', 4), ('Thread-5', 5)]
        # *zip(*args): [('Thread-1', 'Thread-2', 'Thread-3', 'Thread-4', 'Thread-5'), (1, 2, 3, 4, 5)]
        executor.map(log_service, *zip(*args))
        sleep(10)
        logging = False
