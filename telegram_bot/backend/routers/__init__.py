from fastapi import APIRouter

from .user import router as user_router

router = APIRouter()
router.include_router(router=user_router, prefix='/user')
