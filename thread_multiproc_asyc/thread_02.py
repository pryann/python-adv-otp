from threading import Thread
from time import ctime, sleep, time


def log_service(thread_name, delay):
    while True:
        sleep(delay)
        print(f"{thread_name}: {ctime(time())}")


if __name__ == "__main__":
    Thread(target=log_service, args=("Thread-1", 1.1), daemon=True).start()
    Thread(target=log_service, args=("Thread-2", 3), daemon=True).start()
    print("Do main stuff")
    sleep(10)
    print("Main thread done")
