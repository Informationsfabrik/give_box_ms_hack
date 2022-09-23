from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from routers.utils import get_db
import models
import schemas

router = APIRouter()


@router.get("/comments/")
def get_comments(
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> schemas.Comment:
    comments = db.query(models.Comment)

    return comments
