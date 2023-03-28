from fastapi import APIRouter

from address.v1 import views

router = APIRouter(prefix="/address")

router.include_router(views.router)
