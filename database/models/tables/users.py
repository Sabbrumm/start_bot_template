from sqlalchemy import Integer, Column, BigInteger, String, Null, Boolean, LargeBinary

from database import base

class User(base.Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, unique=True)