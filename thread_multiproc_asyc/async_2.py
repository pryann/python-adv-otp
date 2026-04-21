import asyncio
import re
from time import perf_counter


async def get_http_request(id):
    print(f"GET request {id} started...")
    await asyncio.sleep(2)
    print(f"GET request {id} done")
    return f"Get data {id}"


async def post_http_request():
    print("POST request started...")
    await asyncio.sleep(4)
    print("POST request done")
    return "Post data"


# async def main():
#     get = asyncio.create_task(get_http_request())
#     post = asyncio.create_task(post_http_request())
#     # tuple like, not awaited yet, only the first one is awited
#     # await post, get
#     await get
#     await post
#     print(f"Get response: {get.result()}, Post response: {post.result()}")


async def main():
    requests = [get_http_request(i + 1) for i in range(100)]
    await asyncio.gather(*requests)


if __name__ == "__main__":
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()
    print(f"Execution time: {end_time - start_time: .6f} sec")
