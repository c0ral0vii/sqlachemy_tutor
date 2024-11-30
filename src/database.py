from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, URL, text
from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    poll_size=5,
    max_overflow=10,
)

with engine.connect() as connection:
    res = connection.execute(text("SELECT VERSION()"))
    print(f"{res=}")