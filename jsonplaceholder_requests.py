"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(url: str, session: aiohttp.ClientSession) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_users(session: aiohttp.ClientSession) -> list[dict]:
    return await fetch_json(USERS_DATA_URL, session)


async def fetch_posts(session: aiohttp.ClientSession) -> list[dict]:
    return await fetch_json(POSTS_DATA_URL, session)


async def main():
    async with aiohttp.ClientSession() as session:
        users = await fetch_users(session)
        print(f"Users: {len(users)}")

        posts = await fetch_posts(session)
        print(f"Posts: {len(posts)}")


if __name__ == "__main__":
    asyncio.run(main())
