from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Product
from ..schemas import ProductSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products", response_model=List[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.order).all()
    return products
