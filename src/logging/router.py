from typing import Optional

from fastapi import APIRouter, Request

from src.logging.logging import logger

router = APIRouter(
    prefix="",
    tags=["Logging"]
)


@router.get("/logger")
async def write_logging(type: str, message: str):
    if type == "ERROR":
        logger.error(message)
    if type == "INFO":
        logger.info(message)
    if type == "WARNING":
        logger.warning(message)


@router.post("/logger_frontend")
async def write_logging(request: Request):
    try:
        data = await request.json()
        type = data.get("type")
        message = data.get("message")
        if type == "ERROR":
            logger.error(message)
        if type == "INFO":
            logger.info(message)
        if type == "WARNING":
            logger.warning(message)
        return {"status": "success"}
    except Exception as e:
        return {"status": 500, "message": str(e)}


