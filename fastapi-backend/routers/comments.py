from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import models
import schemas
from utils import get_db

router = APIRouter()


@router.get("/comments/{box_id}")
def get_comments(box_id: int, db: Session = Depends(get_db)) -> List[schemas.Comment]:

    comments = db.query(models.Comment).filter(models.Comment.box_id == box_id).all()
    comments = [schemas.Comment(**comment.__dict__) for comment in comments]
    return comments


@router.post("/comments")
def post_comment(comment: schemas.Comment, db: Session = Depends(get_db)) -> int:

    comment_dict = comment.dict()
    user_id = comment_dict["user_id"]
    box_id = comment_dict["box_id"]

    user = db.query(models.User).filter(models.User.id == user_id).first()
    box = db.query(models.GiveBox).filter(models.GiveBox.id == box_id).first()

    assert user is not None
    assert box is not None

    comment = models.Comment(**comment.dict())
    comment.user = user
    comment.box = box

    timestamp = datetime.now()
    comment.timestamp = timestamp

    db.add(comment)
    db.commit()

    return comment.id
