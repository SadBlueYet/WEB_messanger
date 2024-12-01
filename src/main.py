from fastapi import FastAPI

from routers import all_routers
from fastapi.staticfiles import StaticFiles

from config import settings

app = FastAPI(title="Web messanger")

app.mount("/static", StaticFiles(directory="static"), name="static")

for router in all_routers:
    app.include_router(router)
print(settings.DATABASES.ASYNC_POSTGRES_DSN)