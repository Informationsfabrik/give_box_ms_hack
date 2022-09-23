from audioop import add
import schemas
import models
from database import SessionLocal
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

    db_box = db.query(models.GiveBox).filter(models.GiveBox.id == id_).first()
    
    box_dict = db_box.__dict__
    
    box : schemas.GiveBox = schemas.GiveBox(**box_dict)

    return box


@router.get("/givebox")
def get_givebox_list(
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> List[schemas.GiveBoxBase]:
    # Authorize.jwt_required()

    boxes = db.query(models.GiveBox).all()

    boxes = [schemas.GiveBoxBase(**box.__dict__) for box in boxes]

    return boxes


@router.post("/add_givebox")
def add_givebox(box: schemas.GiveBox, db: SessionLocal = Depends(get_db)):
    new_box = models.GiveBox(**box.__dict__)
    db.add(new_box)
    db.commit()
    return 200

