import uuid

from src import db


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(120), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)

    def __init__(self, title, release_date, description, distributed_by, length, rating):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'Film({self.title}, {self.uuid}, {self.release_date})'

    def to_dict(self):
        return {
            'title': self.title,
            'uuid': self.uuid,
            'release_date': self.release_date.strftime('%Y-%m-%d'),
            'description': self.description,
            'distributed_by': self.distributed_by,
            'length': self.length,
            'rating': self.rating,
        }
