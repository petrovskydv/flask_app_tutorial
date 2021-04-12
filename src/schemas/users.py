from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('id', 'is_admin')
        load_only = ('password',)
