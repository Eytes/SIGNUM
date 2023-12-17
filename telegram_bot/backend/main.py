from fastapi import FastAPI

from telegram_bot.backend.routers.user import router as user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='SIGNUM telegram bot backend'
    )

    app.include_router(user_router)

    return app


app = create_app()
