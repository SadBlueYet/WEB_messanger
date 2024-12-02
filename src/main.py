from fastapi import FastAPI

from routers import all_routers
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse
from config import settings

app = FastAPI(title="Web messanger")

app.mount("/static", StaticFiles(directory="static"), name="static")

for router in all_routers:
    app.include_router(router)


@app.exception_handler(IntegrityError)
async def handle_integrity_error(request, exc):
    if "DETAIL:  Key (username)=(string) already exists" in str(exc.orig):
        return JSONResponse(
            status_code=400,
            content={"detail": "User with this field already exists."},
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected database error occurred."},
    )