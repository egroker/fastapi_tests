from .config import *

from fastapi import FastAPI
import asyncpg

app = FastAPI(title="My cool application")

# Create a single connection pool for the application
db_pool = None # type: asyncpg.Pool

@app.on_event("startup")
async def startup_event():
    """
    This event is triggered when the application starts up.
    It creates the connection pool for the application.
    """
    global db_pool
    db_pool = await asyncpg.create_pool(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )

@app.on_event("shutdown")
async def shutdown_event():
    """
    This event is triggered when the application is shutting down.
    It closes the connection pool.
    """
    await db_pool.close()

async def get_db() -> asyncpg.Connection:
    """
    This function acquires a connection from the application's connection pool.
    """
    #async with db_pool.acquire() as conn:
    #    yield conn
    """
    Or we can use simple connection creation
    """
    #async with asyncpg.connect(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}') as conn:
    #    yield conn
    conn = await asyncpg.connect(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    try:
        yield conn
    finally:
        conn.close()