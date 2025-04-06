from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

import config


engine = create_async_engine(
    config.SQLA_PG_URL,
    echo=config.SQLA_ECHO,
)

session = async_sessionmaker(engine, expire_on_commit=False)