from datetime import datetime
from sqlite3 import Timestamp
from pydantic import BaseModel
from typing import Optional, List, Dict


class GiveBoxBase(BaseModel):
    id: Optional[int]
    longitude: float
    latitude: float
    is_temporary: Optional[bool]
    description: Optional[str]
    opening_hours: Optional[str]
    is_temporary: Optional[bool]
    extern_link: Optional[str]
    content: Optional[dict]


class GiveBox(GiveBoxBase):
    maintenance_needed: Optional[bool]
    maintainer_info: Optional[str]
    last_confirmation_date: Optional[datetime]
    image_id: Optional[str]
    street: Optional[str]
    house_number: Optional[int]
    zip_code: Optional[int]
    city: Optional[str]





class UserBase(BaseModel):
    id: Optional[int]
    lastname: str
    firstname: str


class User(UserBase):
    email: str
    password: str
    street: str
    house_number: int
    zip_code: int
    city: str

class Comment(BaseModel):
    user: User
    box: GiveBox
    text: str
    timestamp: datetime
