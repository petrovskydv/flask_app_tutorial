from flask_restful import Resource


class Smoke(Resource):
    def get(self):
        return {'massage': 'OK'}, 200
