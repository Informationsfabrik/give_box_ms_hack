import json

from sqlalchemy.orm import Session

import models
from database import Base
from database import SessionLocal

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_base_data(router: str, db: Session, model: Base) -> None:
    with open(f"data/{router}.json") as json_file:
        data = json.load(json_file)

    for item in data:
        # insert data into database
        db_item = model(**item)
        db.add(db_item)
        db.commit()


def init_db(db: Session) -> None:
    db_box = db.query(models.GiveBox).first()
    if not db_box:
        # load sample data from json
        load_base_data(router="giveboxes", db=db, model=models.GiveBox)
        load_base_data(router="users", db=db, model=models.User)


if __name__ == "__main__":
    init_db(db=SessionLocal())
