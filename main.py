"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import aiohttp
from jsonplaceholder_requests import fetch_users, fetch_posts
from typing import List, Dict
from sqlalchemy.ext.asyncio import async_session

from models import (
    User,
    Post,
)
from models.db import session


async def fetch_users_data(
        http_session: aiohttp.ClientSession
) -> List[Dict]:
    all_users = await fetch_users(http_session)
    return [{
        "name": user.get("name", ""),
        "username": user.get("username", ""),
        "email": user.get("email", ""),
        "website": user.get("website", ""),
    } for user in all_users]


async def fetch_posts_data(
        http_session: aiohttp.ClientSession
) -> List[Dict]:
    all_posts = await fetch_posts(http_session)
    return [{
        "title": post.get("title", ""),
        "body": post.get("body", ""),
        "user_id": post.get("user_Id", ""),
    } for post in all_posts]

async def create_users_and_post(session: session):
    async with aiohttp.ClientSession() as http_session:
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(http_session),
            fetch_posts_data(http_session),
        )
        for user_data in users_data:
            user = User(**user_data)
            session.add(user)
            print("Created user:", user)
        await session.commit()

        for post_data in posts_data:
            post = Post(**post_data)
            session.add(post)
            print("Created post:", post)
        await session.commit()



async def main():
    async with async_session() as session:
        await create_users_and_post(session)


if __name__ == "__main__":
    asyncio.run(main())
