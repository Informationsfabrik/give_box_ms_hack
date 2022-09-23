from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from typing import List
from sqlalchemy.orm import Session
from routers.utils import get_db
import models
import schemas

router = APIRouter()


@router.get("/givebox/{id_}")
def get_givebox_by_id(
    id_: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> schemas.GiveBox:
    # Authorize.jwt_required()

    box = db.query(models.GiveBox).filter(models.GiveBox.id == id_).first()

    return schemas.GiveBox(**box.__dict__)


@router.get("/givebox")
def get_givebox_list(
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> List[schemas.GiveBoxBase]:
    # Authorize.jwt_required()

    boxes = db.query(models.GiveBox).all()

    boxes = [schemas.GiveBoxBase(**box.__dict__) for box in boxes]

    return boxes
