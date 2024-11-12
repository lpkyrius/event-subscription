from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Question, QuestionOption, Answer
from ..schemas import QuestionSchema, AnswerSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/questions", response_model=List[QuestionSchema])
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(Question).order_by(Question.order).all()
    response = []
    for question in questions:
        options = db.query(QuestionOption).filter(QuestionOption.question_id == question.id).order_by(QuestionOption.order).all()
        response.append({
            "id": question.id,
            "text": question.text,
            "type": question.type,
            "options": [{"id": opt.id, "text": opt.text} for opt in options]
        })
    return response

@router.post("/submit")
def submit_answers(answers: List[AnswerSchema], db: Session = Depends(get_db)):
    for answer in answers:
        db_answer = Answer(question_id=answer.question_id, answer_text=answer.answer_text)
        db.add(db_answer)
    db.commit()
    return {"status": "submitted"}
