import settings
import uvicorn
from fastapi import FastAPI
from loguru import logger

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    logger.info(f"DEBUG = {settings.DEBUG}")

    if settings.DEBUG:
        uvicorn.run("main:app", reload=True, port=settings.PORT)
    else:
        uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT)
