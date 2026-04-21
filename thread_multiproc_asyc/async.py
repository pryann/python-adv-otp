import asyncio
from time import perf_counter


async def http_request():
    print("Task started...")
    await asyncio.sleep(2)
    print("Task done")


async def main():
    print(f"get: {await http_request()}")


if __name__ == "__main__":
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time: .6f} sec")
