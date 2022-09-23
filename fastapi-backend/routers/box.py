from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from utils import get_db
import models

router = APIRouter()


class GiveBoxBase(BaseModel):
    id: int
    longitide: float
    latitude: float
    address: str
    is_temporary: bool
    description: str
    opening_hours: str


class GiveBox(GiveBoxBase):
    last_checked: datetime
    maintenance_needed: bool
    maintainer_information: Optional[str]
    last_confirmation_date: datetime
    # maintainer


@router.get("/givebox/{id_}")
def get_givebox_by_id(
    id_: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> GiveBox:
    Authorize.jwt_required()

    box = db.query(models.GiveBox).filter(models.GiveBox.id == id_).first()

    return GiveBox(box)


@router.get("/givebox")
def get_givebox_list(
    db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
) -> List[GiveBoxBase]:
    Authorize.jwt_required()

    box = db.query(models.GiveBox)

    return GiveBox(box)
