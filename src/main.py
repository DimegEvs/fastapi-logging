from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.logging.router import router as router_logging
app = FastAPI()

app.include_router(router_logging)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  # Здесь нужно указать разрешенные домены
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)