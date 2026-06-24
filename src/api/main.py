from typing import Optional, List

from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session

from .models import orm, crud
from .models.db import SessionLocal, engine
from .models.schema import UserSchema, ItemSchema

orm.Base.metadata.create_all(bind=engine)

api = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.post("/users/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@api.get("/users/", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@api.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@api.post("/users/{user_id}/items/", response_model=ItemSchema)
def create_item_for_user(
        user_id: int, item: ItemSchema, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@api.get("/items/", response_model=List[ItemSchema])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@api.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}


@api.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@api.get("/users/{role_name}")
async def get_model(role_name: orm.Role):
    if role_name == orm.Role.anonymous:
        return {"role_name": role_name, "users": "[]"}
    return {"role_name": role_name, "users": "[Teste]"}


@api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@api.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    items = []  # retornar todos os itens
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@api.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemSchema):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
