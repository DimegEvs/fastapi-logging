import os
from typing import Optional, Dict

from fastapi import APIRouter, Request
from src.logging.logging import UserLogger, logger
import logging

# Создание роутера для логирования
router = APIRouter(
    prefix="",
    tags=["Logging"]
)

# Словарь для хранения логгеров пользователей
user_loggers: Dict[int, UserLogger] = {}

# Эндпоинт для записи логов
@router.get("/logger")
async def write_logging(type: str, message: str, user_id: int):
    print(user_loggers)
    if user_id not in user_loggers:
        user_loggers[user_id] = UserLogger(user_id)  # Создание нового логгера для пользователя, если его нет в словаре
    user_logger = user_loggers[user_id]
    if type == "ERROR":
        user_logger.log_error(message)
    if type == "INFO":
        user_logger.log_info(message)
    if type == "WARNING":
        user_logger.log_warning(message)

# Эндпоинт для записи логов с фронтенда
@router.post("/logger_frontend")
async def write_logging(request: Request):
    try:
        data = await request.json()  # Получение данных из запроса
        type = data.get("type")
        message = data.get("message")
        user_id = int(data.get("user_id"))
        if user_id not in user_loggers:
            user_loggers[user_id] = UserLogger(user_id)  # Создание нового логгера для пользователя, если его нет в словаре
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

# Эндпоинт для записи логов промежуточного ПО
@router.get("/logger_middleware")
async def write_logging_middleware(message: str):
    logger.debug(message)  # Запись сообщения в логгер
