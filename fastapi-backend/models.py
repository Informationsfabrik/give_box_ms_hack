from importlib.metadata import metadata
from tokenize import Number
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime, JSON, Table
from sqlalchemy.orm import relationship
from database import Base

class Address(Base):
    __tablename__ = "Addresses"
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    house_number = Column(Integer)
    zip_code = Column(Integer)
    city = Column(String)

class Comment(Base):
    __tablename__ = "Comments"
    id = Column(Integer, primary_key=True, index=True)
    box_id = Column(Integer, ForeignKey("Giveboxes.id"), nullable = False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable = False)
    text = Column(String)
    timestamp = Column(DateTime)

user_givebox_association = Table(
    "user_givebox_association",
    Base.metadata,
    Column("user_id", ForeignKey("Users.id")),
    Column("box_id", ForeignKey("Giveboxes.id")),
)

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(Integer, ForeignKey("Addresses.id"), nullable = False)
    giveboxes = relationship("GiveBox", secondary=user_givebox_association,back_populates="maintainer")

class GiveBox(Base):
    __tablename__ = "GiveBoxes"
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    address = Column(Integer, ForeignKey("Addresses.id"), nullable = False)
    opening_hours = Column(String)
    is_temporary = Column(Boolean)
    description = Column(String)
    last_confirmation_date = Column(DateTime)
    maintainer = relationship("User", secondary=user_givebox_association,back_populates="giveboxes")
    image_link = Column(String)
    tags = Column(JSON)



