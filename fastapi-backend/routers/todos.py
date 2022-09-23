from fastapi import APIRouter
from fastapi import Depends, Request
from fastapi.params import Form
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse
from database import SessionLocal
from models import Todo, Givebox

router = APIRouter()


# Helper function to access DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def home(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {"todo_list": todos}


@router.post("/add")
def add(title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = Todo(title=title)
    db.add(new_todo)
    db.commit()

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@router.post("/add_box")
def add_box(box: dict, db: Session = Depends(get_db)):
    new_todo = Givebox(**box)
    pass
    # db.add(new_todo)
    # db.commit()
    #
    # url = router.url_path_for("home")
    # return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@router.get("/update/{todo_id}")
def update(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@router.get("/delete/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()

    url = router.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
