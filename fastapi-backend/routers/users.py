from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Form
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session


from models import User
from routers.todos import get_db

router = APIRouter()


@router.post('/login')
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    user = db.query(User).filter_by(username=username).first()
    if user is None or user.password != password:
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=username)
    return {"access_token": access_token}


@router.post('/register')
def register(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    user = db.query(User).filter_by(username=username).first()
    if user is None or username != user.username:
        new_user = User(username=username, password=password)
        db.add(new_user)
        db.commit()
        access_token = Authorize.create_access_token(subject=username)
        return {"access_token": access_token}
    return {"Smth went wrong... douee"}
