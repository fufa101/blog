from fastapi import FastAPI
from . import schemas
from .models import Base
from .database import engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.post("/blog")
def create_blog(request: schemas.Blog):
    return {"title": request.title, "body": request.body}
