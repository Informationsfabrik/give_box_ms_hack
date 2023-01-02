from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal
from utils import get_db

router = APIRouter()


@router.get("/users/{id_}")
def get_user_by_id(id_: int, db: Session = Depends(get_db)) -> schemas.User:

    user = db.query(models.User).filter(models.User.id == id_).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return models.User(**user.__dict__)


@router.get("/users")
def get_user(db: Session = Depends(get_db)) -> List[models.User]:

    return db.query(models.User).all()


@router.post("/users")
def add_user(user: schemas.User, db: SessionLocal = Depends(get_db)) -> int:
    new_user = models.User(**user.__dict__)
    db.add(new_user)
    db.commit()
    return new_user.id
