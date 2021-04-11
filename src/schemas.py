from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models import Film, Actor


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True


class ActorSchema(SQLAlchemyAutoSchema):
    model = Actor
    load_instance = True
