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


@router.get("/address/{id_}")
def get_givebox_by_id(
    id_: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> schemas.Address:
    # Authorize.jwt_required()

    address = db.query(models.Address).filter(models.Address.id == id_).first()

    return schemas.Address(**address.__dict__)
