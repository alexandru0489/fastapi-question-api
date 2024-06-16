from sqlalchemy import Column, String
from .database import Base


class User(Base):
    __tablename__ = "users"
    
    username = Column(String, primary_key=True, index=True)
    password = Column(String)

class Question(Base):
    __tablename__ = "questions"

    question = Column(String, primary_key=True, index=True)
    subject = Column(String, index=True)
    correct = Column(String)
    use = Column(String)
    responseA = Column(String)
    responseB = Column(String)
    responseC = Column(String)
    responseD = Column(String, nullable=True)
    remark = Column(String, nullable=True)