import email
from tokenize import Number
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(Integer, ForeignKey("Addresses.id"), nullable = False)


class Address(Base):
    __tablename__ = "Addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    house_number = Column(Integer)
    zipcode = Column(Integer)
    city = Column(String)

class Givebox(Base):
    __tablename__ = "Giveboxes"

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    address = Column(Integer, ForeignKey("Addresses.id"), nullable = False)
    opening_hours = Column(String)
    is_temporary = Column(Boolean)
    description = Column(String)
    last_confirmation_date = Column(DateTime)
    maintainer = Column()

class Comment(Base):
    __tablename__ = "Comments"




