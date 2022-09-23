from datetime import datetime
from pydantic import BaseModel
from typing import Optional


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
