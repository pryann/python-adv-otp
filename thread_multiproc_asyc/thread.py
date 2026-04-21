from threading import Thread, current_thread
from time import perf_counter, sleep


thread = current_thread()
print(thread)


def task():
    print("Task started...")
    sleep(2)
    print("Task done")


if __name__ == "__main__":
    start_time = perf_counter()
    # t1 = Thread(target=task)
    # t2 = Thread(target=task)
    # t3 = Thread(target=task)

    # t1.start()
    # t2.start()
    # t3.start()

    # t1.join()
    # t2.join()
    # t3.join()

    threads = [Thread(target=task) for _ in range(3)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time: .6f} sec")
