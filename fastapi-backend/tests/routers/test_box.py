from routers.box import get_givebox_by_id, get_givebox_list
from routers.utils import get_db
import schemas
from typing import List


def test_get_givebox_by_id():
    box: schemas.GiveBox = get_givebox_by_id(1, get_db())

    assert box is not None
    assert box.id > 0


def test_get_givebox_by_id():
    boxes: List[schemas.GiveBoxBase] = get_givebox_list(get_db())

    assert boxes is not None
    assert len(boxes) > 0
