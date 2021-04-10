from datetime import datetime

from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Film


class Smoke(Resource):
    def get(self):
        return {'massage': 'OK'}, 200


class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return [film.to_dict() for film in films], 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        return film.to_dict(), 200

    def post(self):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                distributed_by=film_json['distributed_by'],
                description=film_json['description'],
                length=film_json['length'],
                rating=film_json['rating']
            )
            print(film)
            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully'}, 201

    def put(self, uuid):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Film).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                    distributed_by=film_json['distributed_by'],
                    description=film_json['description'],
                    length=film_json['length'],
                    rating=film_json['rating']
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 201

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        film_json = request.json
        title = film_json.get('title')
        release_date = datetime.strptime(film_json.get('release_date'), '%B %d, %Y') if film_json.get(
            'release_date') else None
        distributed_by = film_json.get('distributed_by')
        description = film_json.get('description')
        length = film_json.get('length')
        rating = film_json.get('rating')
        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif description:
            film.description = description
        elif length:
            film.length = length
        elif rating:
            film.rating = rating
        db.session.add(film)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return '', 404
        db.session.delete(film)
        db.session.commit()
        return '', 204


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
