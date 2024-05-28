from app import app
from app.app import get_db
from requests.requests import *
from fastapi import Depends, Path, Query, Form
from typing_extensions import Annotated
from typing import Union
from models import User, person_regexp


@app.get("/users")
async def read_users(db: asyncpg.Connection=Depends(get_db)):
    return await get_users(db)

@app.get("/timelogs/{timelog_id}")
#Here we use PATH to describe this variable - title and validation
async def read_timelog_by_id(timelog_id: Annotated[int, Path(title="The ID of the timelog to get")], db: asyncpg.Connection=Depends(get_db)):
    return await get_timelog_by_id(timelog_id, db)

@app.post("/create_user")
#async def post_user(name: str, mail: str, password: str, db: asyncpg.Connection=Depends(get_db)):
# ------ We can validate mail and password via Annotate
async  def post_user(first_name: Annotated[str, Query(max_length=70, pattern=person_regexp)], mail: Annotated[Union[str,None], Query(max_length=320)], db: asyncpg.Connection=Depends(get_db)):
    return await create_user(db, first_name, mail)

@app.post("/create_user_pydantic")
async def post_user_pydantic(user: User, db: asyncpg.Connection=Depends(get_db)):
    return user

@app.post("/login/")
# We can use Form for some user-inputs, like for login-password
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

@app.get("/")
async def hello():
    return {"msg": "Hello World!"}