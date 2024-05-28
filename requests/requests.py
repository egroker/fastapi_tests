import asyncpg
from fastapi import HTTPException

async def get_users(db):
    #async with db.transaction():
    rows = await db.fetch("SELECT id, name, mail FROM users")
    return [{"id":row[0], "name":row[1], "mail":row[2]} for row in rows]

async def get_timelog_by_id(timelog_id, db):
    async with db.transaction():
        rows = await db.fetch(f"SELECT * FROM timelogs WHERE id={timelog_id}")
        return [{"id":row[0], "content":row[1], "project_id":row[2], "user_id":row[3]} for row in rows]

async def create_user(db: asyncpg.Connection, name, mail):
    async with db.transaction():
    # asyncpg transaction rolls back if there were an exception with sql query, otherwise I'm not sure how it works
    # it looks like that's okay, but I don't like it:)
    #https://stackoverflow.com/questions/12423218/postgresql-wrong-auto-increment-for-serial
        query = "INSERT INTO person (first_name, email) VALUES ($1, $2) RETURNING id, first_name, email"
        try:
            person = await db.fetchrow(query, name, mail)
            result = dict(person)
            return result
        except Exception:
            raise HTTPException(status_code=404, detail="Problems occured")