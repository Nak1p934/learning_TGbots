import asyncio
from models import Base
from session import engine
from models import sms

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def main():
    # await drop_table()
    await create_tables()

if __name__ == "__main__":
    asyncio.run(main())
