from fastapi import APIRouter

from config import settings
from .user import router as user_router

router = APIRouter()
router.include_router(router=user_router, prefix=settings.prefix_user_router)
