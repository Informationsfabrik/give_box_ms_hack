import os
from pathlib import Path

import models
import schemas
from database import SessionLocal
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from utils import get_db

router = APIRouter()

IMAGE_DIR: str = "data/images"


@router.post("/images")
def post_image(image: schemas.Image, db: SessionLocal = Depends(get_db)):

    image_dict = image.__dict__
    box_id = image_dict["box_id"]
    data = image_dict["data"]
    is_title_image = image_dict["is_title_image"]

    assert box_id is not None
    assert data is not None

    box: models.GiveBox = (
        db.query(models.GiveBox).filter(models.GiveBox.id == box_id).first()
    )

    assert box is not None

    image = models.Image()
    image.box = box
    db.add(image)
    db.commit()

    image_id: int = image.id
    path: str = f"{IMAGE_DIR}/{image_id}"
    image.path = path
    image.is_title_image = is_title_image

    db.commit()

    data_as_bytes = bytes(data, "utf-8")

    if not os.path.exists(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)

    with open(path, "wb") as binary_file:

        # Write bytes to file
        binary_file.write(data_as_bytes)

    return image.id


@router.get("/titleimages/{box_id}")
def get_title_image_by_box_id(
    box_id: int, db: Session = Depends(get_db)
) -> schemas.Image:
    db_image = (
        db.query(models.Image)
        .filter(models.Image.box_id == box_id)
        .filter(models.Image.is_title_image is True)
        .first()
    )
    image_dict = db_image.__dict__

    path = image_dict["path"]

    if Path(path).exists() is False:
        raise HTTPException(status_code=404, detail="Image not found")

    with open(path, "rb") as binary_file:
        print(binary_file)
        # Write bytes to file
        data = binary_file.read()

    image = schemas.Image(**image_dict)
    image.data = data

    return image
