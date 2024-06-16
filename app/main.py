from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import SessionLocal, init_db, load_data
from typing import List

# Initialize the database and load data
init_db()
load_data()

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    

@app.get("/questions/", response_model=List[schemas.Question])
def read_questions(use: str, subjects: List[str], limit: int = 10, db: Session = Depends(get_db), username: str = Depends(auth.get_current_user)):
    """
    Retrieve a list of questions.
    
    """
    questions = crud.get_questions(db, use, subjects, limit)
    return questions


@app.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db), username: str = Depends(auth.get_current_user)):
    """
    Create a new question (admin only).
    
    """
    if username != 'admin':
        raise HTTPException(status_code=403, detail="Not authorized")
    return crud.create_question(db, question)