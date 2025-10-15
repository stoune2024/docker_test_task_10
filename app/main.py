from fastapi import FastAPI, HTTPException
from config import settings
from uvicorn import run
import asyncpg


app = FastAPI()


@app.get("/")
def root():
    return {
        "db_url": settings.database_url,
        "host_port": settings.APP_HOST_PORT,
        "container_port": settings.APP_CONTAINER_PORT,
    }


@app.get("/db-check")
async def db_check():
    """
    Проверяет подключение к базе данных PostgreSQL и возвращает её версию.
    """
    conn = None
    try:
        conn = await asyncpg.connect(
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB,
        )
        version = await conn.fetchval("SELECT version();")
        return {"status": "ok", "postgres_version": version}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")
    finally:
        if conn:
            await conn.close()


if __name__ == "__main__":
    run(
        app="main:app",
        reload=True,
        log_level="debug",
        host=settings.APP_HOST,
        port=settings.APP_CONTAINER_PORT,
    )
