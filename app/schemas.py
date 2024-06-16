from pydantic import BaseModel
from typing import Optional

class QuestionBase(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: Optional[str] = None
    remark: Optional[str] = None
      
class  QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    class Config:
        orm_mode = True
