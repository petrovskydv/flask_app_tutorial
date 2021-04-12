import pathlib

BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kjseyhf834iwebfski3ry49gfiewvo84h93bgiegdsd'
