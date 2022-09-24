import os
from database import SessionLocal
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session, joinedload
from utils import get_db
import models
import schemas

router = APIRouter()

IMAGE_DIR : str = "data/images"

@router.post("/images")
def post_image(image: schemas.Image, db: SessionLocal = Depends(get_db)):
    
    image_dict = image.__dict__
    box_id = image_dict["box_id"]
    data = image_dict["data"]
    is_title_image = image_dict["is_title_image"]

    assert box_id is not None
    assert data is not None

    box : models.GiveBox = db.query(models.GiveBox).filter(models.GiveBox.id == box_id).first()

    assert box is not None

    image = models.Image()
    image.box = box
    db.add(image)
    db.commit()

    image_id : int = image.id 
    path : str = f"{IMAGE_DIR}/{image_id}"
    image.path = path
    image.is_title_image = is_title_image

    db.commit()

    data_as_bytes = bytes(data, 'utf-8')


    if not os.path.exists(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)

    with open(path, "wb") as binary_file:
   
        # Write bytes to file
        binary_file.write(data_as_bytes)


    return 200
