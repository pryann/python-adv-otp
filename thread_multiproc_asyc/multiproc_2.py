from time import perf_counter, sleep

import concurrent.futures as cf


def proc_task(sec):
    sleep(sec)
    return f"Value: {sec}"


def main():
    with cf.ProcessPoolExecutor() as ex:
        results = [ex.submit(proc_task, i) for i in range(10)]
        for result in cf.as_completed(results):
            print(result.result())


if __name__ == "__main__":
    start_timer = perf_counter()
    main()
    end_timer = perf_counter()
    print("excecution time: ", end_timer - start_timer)
