from fastapi import FastAPI

from config import settings
from routers import router

app = FastAPI(title="SIGNUM telegram bot backend")
app.include_router(router=router, prefix=settings.prefix_api_v1)
