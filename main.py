import asyncio
from fastapi import FastAPI, HTTPException
import aiopg

app = FastAPI()

# Connect to PostgreSQL database
dsn = f'dbname=postgres user=postgres password=postgres host=localhost:5432'

# Handler function to retrieve all rows from users table
async def get_users():
    async with aiopg.connect(dsn) as con:
        async with con.cursor() as cursor:
            query = "SELECT * FROM users"
            await cursor.execute(query)
            result = []
            async for row in cursor:
                result.append(row)
            return result

@app.get("/users")
async def read_users():
    return await get_users()

if __name__ == "__main__":
    # Run the application with Uvicorn (async) server
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)