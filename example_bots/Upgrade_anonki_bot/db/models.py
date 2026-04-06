from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger

Base = declarative_base()

class sms(Base):
    __tablename__ ="sms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    operator_id = Column(BigInteger)
    sender = Column(BigInteger)
    who_sender = Column(String)
    text = Column(String)
    time = Column(String)

