from datetime import datetime
from pydantic import BaseModel, Json
from typing import Optional, List 

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


class Content(BaseModel):
    book: Optional[bool]
    clothes: Optional[bool]
    toys: Optional[bool]
    electronics: Optional[bool]
    other: Optional[str]


class GiveboxBase(BaseModel):
    id: Optional[int]
    longitude: float
    latitude: float
    is_temporary: Optional[bool]
    description: Optional[str]
    opening_hours: Optional[str]
    is_temporary: Optional[bool]
    extern_link: Optional[str]
    content: Optional[Content]


class Givebox(GiveboxBase):
    maintenance_needed: Optional[bool]
    maintainer_info: Optional[str]
    last_confirmation_date: Optional[datetime]
    image_id: Optional[str]
    street: Optional[str]
    house_number: Optional[int]
    zip_code: Optional[int]
    city: Optional[str]
    maintainers : Optional[List[User]]

class Comment(BaseModel):
    user: User
    box: Givebox
    text: str
    timestamp: datetime
