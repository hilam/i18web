from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from api.models.orm import User, Item

UserSchema = sqlalchemy_to_pydantic(User)
ItemSchema = sqlalchemy_to_pydantic(Item)
