from sqlalchemy.orm import Session 
from . import models, schemas

def get_questions(db: Session, use: str, subjects: list, limit: int):
    return  db.query(models.Question).filter(models.Question.use == use, models.Question.subject.in_(subjects)).order_by(func.random()).limit(limit).all()
              
              
def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question