from pathlib import Path
from typing import List

import models
import schemas
from database import SessionLocal
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session, joinedload
from utils import get_db

router = APIRouter()


@router.get("/giveboxes/image/{id_}")
def get_givebox_image(id_: int):
    path = Path(f"data/images/{id_}.jpg")
    if path.exists() is False:
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(path)


@router.get("/giveboxes/{id_}")
def get_givebox_by_id(id_: int, db: Session = Depends(get_db)) -> schemas.Givebox:

    db_box = (
        db.query(models.GiveBox)
        .options(joinedload(models.GiveBox.maintainers))
        .filter(models.GiveBox.id == id_)
        .first()
    )
    if db_box is None:
        raise HTTPException(status_code=404, detail="Givebox not found")

    box_dict = db_box.__dict__
    box_dict["maintainers"] = [
        schemas.User(**maintainer.__dict__) for maintainer in box_dict["maintainers"]
    ]

    return schemas.Givebox(**box_dict)


@router.get("/giveboxes")
def get_givebox_list(db: Session = Depends(get_db)) -> List[schemas.GiveboxBase]:

    boxes = db.query(models.GiveBox).all()
    boxes = [schemas.GiveboxBase(**box.__dict__) for box in boxes]

    return boxes


@router.post("/giveboxes")
def post_givebox(box: schemas.Givebox, db: SessionLocal = Depends(get_db)):
    new_box = models.GiveBox(**box.dict())
    db.add(new_box)
    db.commit()
    return new_box.id
