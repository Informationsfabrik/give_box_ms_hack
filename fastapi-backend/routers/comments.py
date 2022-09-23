from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from starlette import status
from sqlalchemy.orm import Session
from utils import get_db
import models
import schemas

router = APIRouter()


@router.get("/comments/")
def get_comments(db: Session = Depends(get_db)) -> schemas.Comment:
    comments = db.query(models.Comment)

    return comments


@router.post("/comments")
def post_comment(text: str, user_id: int, box_id: int, db: Session = Depends(get_db)):
    comment = schemas.Comment(text=text, user_id=user_id, box_id=box_id)
    db.add(comment)
    db.commit()

    url = router.url_path_for("givebox")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
