from datetime import datetime
from sqlite3 import Timestamp
from pydantic import BaseModel
from typing import Optional, List, Dict


class Address(BaseModel):
    id: int
    street: str
    house_number: int
    zip_code: int
    city: str

class GiveBoxBase(BaseModel):
    id: Optional[int]
    longitude: float
    latitude: float
    address: Address# Dict[str, any]
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





class UserBase(BaseModel):
    id: int
    lastname: str
    firstname: str
    # address


class User(UserBase):
    email: str
    passwort: str
    address: Address
    giveboxes: List[GiveBox]


class Comment(BaseModel):
    user: User
    box: GiveBox
    text: str
    timestamp: datetime
