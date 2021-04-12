from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import User


class UserSchema(SQLAlchemyAutoSchema):
    model = User
    load_instance = True
