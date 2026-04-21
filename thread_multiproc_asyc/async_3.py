import asyncio
import aiohttp


async def get_http_request(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/photos",
    ]
    tasks = [get_http_request(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    print(responses)


if __name__ == "__main__":
    asyncio.run(main())
