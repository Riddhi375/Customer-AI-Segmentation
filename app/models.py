from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    email = Column(String(100), unique=True)

    age = Column(Integer)

    city = Column(String(100))

    gender = Column(String(20))