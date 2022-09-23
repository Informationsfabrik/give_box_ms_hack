from database import SessionLocal
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from routers.utils import get_db
import models
import schemas

router = APIRouter()


@router.get("/users/{id_}")
def get_user_by_id(
    id_: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> schemas.User:
    # Authorize.jwt_required()

    user = db.query(models.User).filter(models.User.id == id_).first()

    return schemas.User(user)


@router.get("/users")
def get_user(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> List[schemas.UserBase]:
    # Authorize.jwt_required()

    users = db.query(models.User)
    users = [schemas.GiveBoxBase(user) for user in users]

    return users

@router.post("/add_user")
def add_givebox(user: schemas.User, db: SessionLocal = Depends(get_db)):
    new_user = models.User(**user.__dict__)
    db.add(new_user)
    db.commit()
    return 200
