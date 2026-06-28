from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine

app = FastAPI()

@app.get("/")
def root():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "message": "Database Connected Successfully 🚀"
    }