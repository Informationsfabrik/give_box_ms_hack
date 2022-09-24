from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from starlette import status
from sqlalchemy.orm import Session
from utils import get_db
import models
import schemas

router = APIRouter()


@router.get("/comments/{box_id}")
def get_comments(box_id:int, db: Session = Depends(get_db)) -> schemas.Comment:
    comments = db.query(models.Comment).filter(models.Comment.id == box_id)

    return comments

@router.post("/comments")
def post_comment(comment :schemas.Comment, db: Session = Depends(get_db)):

    comment_dict = comment.dict()
    user_id = comment_dict["user_id"]
    box_id = comment_dict["box_id"]

    user = db.query(models.User).filter(models.User.id == user_id).first()
    box = db.query(models.GiveBox).filter(models.GiveBox.id == box_id).first()

    comment = models.Comment(**comment.dict())
    comment.user = user
    comment.box = box

    db.add(comment)
    db.commit()

    return 200