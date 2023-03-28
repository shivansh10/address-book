import db
from fastapi import HTTPException, status

from geopy.geocoders import Nominatim

from address import models, schema

loc = Nominatim(user_agent="GetLoc")


class Address:
    
    def __init__(self) -> None:
        self.db = db.get_db
    
    async def create_new_address(self, data: schema.AddressBase):
        
        address = models.Address(address=data.address)
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        
        getLoc = loc.geocode(data.address)
        coordinate = models.Coordinate(
            latitude=getLoc.latitude, 
            longitude=getLoc.longitude, 
            address_id=address.id
            )

        self.db.add(coordinate)
        self.db.commit()
        self.db.refresh(coordinate)

        return coordinate
        
    async def get_address_by_id(self, address_id: int):
        address_info = self.db.query(models.Address).get(address_id)

        if not address_info:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data not found!"
            )

        return address_info
        
    async def delete_address_by_id(self, address_id: int):
        self.db.query(models.Address).filter(
            models.Address.id == address_id).delete()
        self.db.commit()
        return
    
    async def update_address_by_id(self, request, address_id: int):
        address = self.db.query(models.Address).filter_by(id=address_id).first()
        if not address:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Address Not Found !"
            )
        address.address = request.address if request.address else address.address
        self.db.commit()
        self.db.refresh(address)
        return address
    
    async def get_address_details(request_data):
        pass
