from routers import auth, users
from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status":"ok"}


app.include_router(auth.router)
app.include_router(users.router)

# uvicorn main:app --reload