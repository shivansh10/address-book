from decimal import Decimal
from pydantic import BaseModel
from typing import Optional


class AddressBase(BaseModel):
    id: Optional[int]
    created_at: Optional[str]
    address: str

    class Config:
        orm_mode = True


class CoordinateBase(BaseModel):
    latitude: Decimal
    longitude: Decimal
    
    class Config:
        orm_mode = True


class Address(AddressBase, CoordinateBase):
    
    class Config:
        orm_mode = True


class AddressUpdate(BaseModel):
    address: Optional[str]

    class Config:
        orm_mode = True


class AddressList(BaseModel):
    address: Optional[str]

    class Config:
        orm_mode = True

class AddressData(CoordinateBase):
    distance: int
