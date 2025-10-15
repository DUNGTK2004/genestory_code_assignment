from app import models, crud
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, get_db
from dotenv import load_dotenv
import os
import requests 
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud.router, tags=['Tasks'], prefix='/api')

@app.get("/api/healthchecker")
def root():
    return {"Message": "Welcome to FastAPI with SQLAlchemy"}

@app.get("/api/db-healthchecker")
def db_healthchecker(db: Session = Depends(get_db)):
    try:
        # Execute a simple query to check database connectivity
        db.execute(text("SELECT 1"))
        return {"message": "Database is healthy"}
    except OperationalError:
        raise HTTPException(status_code=500, detail="Database is not reachable")
    
@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    try:
        #Make a GET request to the JSONPlaceholder API
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="API call failed")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    