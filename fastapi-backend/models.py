from sqlalchemy import JSON
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

from database import Base

user_givebox_association = Table(
    "user_givebox_association",
    Base.metadata,
    Column("user_id", ForeignKey("Users.id")),
    Column("box_id", ForeignKey("GiveBoxes.id")),
)


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    email = Column(String)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    street = Column(String)
    house_number = Column(Integer)
    zip_code = Column(Integer)
    city = Column(String)
    maintained_boxes = relationship("GiveBox", secondary=user_givebox_association, back_populates="maintainers")


class GiveBox(Base):
    __tablename__ = "GiveBoxes"
    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    longitude = Column(Float)
    latitude = Column(Float)
    opening_hours = Column(String)
    is_temporary = Column(Boolean)
    title = Column(String)
    description = Column(String)
    extern_link = Column(String)
    last_confirmation_date = Column(DateTime, nullable=True)
    maintainer_info = Column(String)
    maintenance_needed = Column(Boolean)
    image_id = Column(String)
    content = Column(JSON, default={}, nullable=True, none_as_null=True)
    street = Column(String)
    house_number = Column(Integer)
    zip_code = Column(Integer)
    city = Column(String)
    maintainers = relationship("User", secondary=user_givebox_association, back_populates="maintained_boxes")


class Comment(Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    box_id = Column(Integer, ForeignKey("GiveBoxes.id"))
    box = relationship("GiveBox")
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User")

    text = Column(String)
    timestamp = Column(DateTime)


class Image(Base):
    __tablename__ = "Images"
    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    box_id = Column(Integer, ForeignKey("GiveBoxes.id"))
    box = relationship("GiveBox")
    path = Column(String)
    is_title_image = Column(Boolean)
