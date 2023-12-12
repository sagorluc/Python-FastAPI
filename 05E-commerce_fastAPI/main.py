from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import *
from registration import registration_router

app = FastAPI()

app.include_router(registration_router)

@app.get('/')
async def home():
    return {'message' : 'Welcome to home'}

register_tortoise(
    app,
    db_url = "sqlite://database.sqlite3", 
    modules = {'models' : ['models']},
    generate_schemas = True,
    add_exception_handlers = True
)