from datetime import datetime
from sqlite3 import Timestamp
from pydantic import BaseModel
from typing import Optional, List, Dict


class GiveBoxBase(BaseModel):
    id: Optional[int]
    longitude: float
    latitude: float
    is_temporary: bool
    description: str
    opening_hours: str
    is_temporary: bool
    extern_link: str
    content = str


class GiveBox(GiveBoxBase):
    last_confirmation_date: datetime
    maintenance_needed: bool
    maintainer_info: Optional[str]
    last_confirmation_date: Optional[datetime]
    image_id: str
    street: str
    house_number: int
    zip_code: int
    city: str





class UserBase(BaseModel):
    id: int
    lastname: str
    firstname: str


class User(UserBase):
    email: str
    passwort: str
    street: str
    house_number: int
    zip_code: int
    city: str
    giveboxes: List[GiveBox]


class Comment(BaseModel):
    user: User
    box: GiveBox
    text: str
    timestamp: datetime
