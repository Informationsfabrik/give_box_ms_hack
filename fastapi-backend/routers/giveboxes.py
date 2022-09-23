from database import SessionLocal
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session, joinedload
from utils import get_db
import models
import schemas

router = APIRouter()


@router.get("/giveboxes/{id_}")
def get_givebox_by_id(id_: int, db: Session = Depends(get_db)) -> schemas.Givebox:

    db_box = db.query(models.GiveBox).options(joinedload(models.GiveBox.maintainers)).filter(models.GiveBox.id == id_).first()
    box_dict = db_box.__dict__
    box_dict["maintainers"] = [schemas.User(**maintainer.__dict__) for maintainer in box_dict["maintainers"]]

    box = schemas.Givebox(**box_dict)

    return box


@router.get("/giveboxes")
def get_givebox_list(db: Session = Depends(get_db)) -> List[schemas.GiveboxBase]:

    boxes = db.query(models.GiveBox).all()
    boxes = [schemas.GiveboxBase(**box.__dict__) for box in boxes]

    return boxes


@router.post("/giveboxes")
def post_givebox(box: schemas.Givebox, db: SessionLocal = Depends(get_db)):
    new_box = models.GiveBox(**box.__dict__)
    db.add(new_box)
    db.commit()
    return 200
