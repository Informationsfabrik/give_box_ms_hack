from datetime import datetime
from sqlite3 import Timestamp
from pydantic import BaseModel
from typing import Optional, List


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


class Address(BaseModel):
    id: int
    street: str
    house_number: int
    zip_code: int
    city: str


class UserBase(BaseModel):
    id: int
    lastname: str
    firstname: str
    # address


class User(UserBase):
    email: str
    passwort: str
    address: Address
    giveboxes: List[int]


class Comment(BaseModel):
    user_id: int
    box_id: int
    text: str
    timestamp: datetime
