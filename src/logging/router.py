import os
from typing import Optional, Dict

from fastapi import APIRouter, Request
from src.logging.logging import UserLogger
import logging


router = APIRouter(
    prefix="",
    tags=["Logging"]
)

user_loggers: Dict[int, UserLogger] = {}

@router.get("/logger")
async def write_logging(type: str, message: str, user_id: int):
    print(user_loggers)
    if user_id not in user_loggers:
        user_loggers[user_id] = UserLogger(user_id)
    user_logger = user_loggers[user_id]
    if type == "ERROR":
        user_logger.log_error(message)
    if type == "INFO":
        user_logger.log_info(message)
    if type == "WARNING":
        user_logger.log_warning(message)


@router.post("/logger_frontend")
async def write_logging(request: Request):
    try:
        data = await request.json()
        type = data.get("type")
        message = data.get("message")
        user_id = int(data.get("user_id"))
        if user_id not in user_loggers:
            user_loggers[user_id] = UserLogger(user_id)
        user_logger = user_loggers[user_id]
        if type == "ERROR":
            user_logger.log_error(message)
        if type == "INFO":
            user_logger.log_info(message)
        if type == "WARNING":
            user_logger.log_warning(message)

        return {"status": "success"}
    except Exception as e:
        return {"status": 500, "message": str(e)}








