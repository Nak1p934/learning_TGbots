from db.session import SessionLocal
from db.models import sms
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import asyncio

async def add_sms(operator_id, sender_id, who_sender, text, time):
    session = SessionLocal()

    smska = sms(operator_id=operator_id, sender=sender_id, who_sender=who_sender, text=text, time=time)
    session.add(smska)
    await session.commit()
    # await session.refresh()
    return smska

async def get_json(session: AsyncSession, operator_id: int) -> dict:
    result = await session.execute(select(sms).where(sms.operator_id == operator_id))

    smski = result.scalars().all()
    return smski

async def get_all_operator_ids(session: AsyncSession) -> list[int]:
    result = await session.execute(
        select(sms.operator_id).distinct()
    )

    # scalars() → достаёт только значения, без кортежей
    operator_ids = result.scalars().all()

    return operator_ids

# if __name__ == "__main__":
#     asyncio.run(get_json(SessionLocal, 1228798145))
