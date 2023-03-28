from decimal import Decimal
from datetime import datetime
from sqlalchemy import Column, Float, ForeignKey, Text, DateTime, Integer

from db import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now)
    address = Column(Text)


class Coordinate(Base):
    latitude: Decimal
    longitude: Decimal
    address_id = Column(Integer, ForeignKey(Address.id, ondelete="CASCADE"))
