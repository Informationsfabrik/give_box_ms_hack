from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from typing import Optional

router = APIRouter()


class Box(BaseModel):
    id: int
    longitide: float
    latitude: float
    address: str
    temporary: bool
    name: str
    last_checked: datetime
    maintenance_needed: bool
    maintainer_information: Optional[str]
    # maintainer
    # öffnungszeiten


@router.get("/box/{id_}")
def items(id_: int, Authorize: AuthJWT = Depends()) -> Box:
    Authorize.jwt_required()

    return {"items": items}
