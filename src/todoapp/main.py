from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.todoapp import models
from src.todoapp.database import engine
from src.todoapp.routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="src/todoapp/static"), name="static")
app.include_router(auth.router)
app.include_router(todos.router)
