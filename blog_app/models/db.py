from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import sys
from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent))
from blog_app.config import settings

engine = create_async_engine(
    url = settings.db.async_url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
