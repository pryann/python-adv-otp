from multiprocessing import Process
from time import perf_counter, sleep


def proc_task():
    sleep(2)


if __name__ == "__main__":
    start_timer = perf_counter()
    # proc_task()
    # proc_task()
    # proc_task()
    p1 = Process(target=proc_task)
    p2 = Process(target=proc_task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_timer = perf_counter()
    print("excecution time: ", end_timer - start_timer)
