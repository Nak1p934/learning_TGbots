# from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine("postgresql+asyncpg://postgres:1234@localhost:5432/mydb", echo=False)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)