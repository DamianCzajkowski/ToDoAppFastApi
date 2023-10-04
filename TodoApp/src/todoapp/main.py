from fastapi import FastAPI
from todoapp import models
from todoapp.database import engine
from todoapp.routers import auth, todos
from fastapi.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="src/todoapp/static"), name="static")
app.include_router(auth.router)
app.include_router(todos.router)
