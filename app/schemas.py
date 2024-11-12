from pydantic import BaseModel
from typing import List, Optional

class QuestionOptionSchema(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True

class QuestionSchema(BaseModel):
    id: int
    text: str
    type: str
    options: List[QuestionOptionSchema] = []

    class Config:
        orm_mode = True

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True

class AnswerSchema(BaseModel):
    question_id: int
    answer_text: Optional[str]
    multiple_choice_selections: Optional[List[int]] = []
    