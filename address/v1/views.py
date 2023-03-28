from fastapi import APIRouter, status, Response
from typing import List

from address import handler, schema

router = APIRouter(prefix="/v1")

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.AddressBase)
async def create_new_address(request: schema.AddressBase):
    result = await handler.create_new_address(request)
    return result


@router.get('/{address_id}', status_code=status.HTTP_200_OK, response_model=schema.AddressBase)
async def get_address_by_id(address_id: int):                            
    return await handler.get_address_by_id(address_id)


@router.delete('/{address_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_address_by_id(address_id: int):
    return await handler.delete_address_by_id(address_id)


@router.patch('/{address_id}', status_code=status.HTTP_200_OK, response_model=schema.AddressBase)
async def update_address_by_id(request: schema.AddressUpdate, address_id: int):                            
    return await handler.update_address_by_id(request, address_id)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schema.AddressList])
async def get_address_details(request_data: schema.AddressData):
    result = await handler.get_address_within_kms(request_data)
    return result
