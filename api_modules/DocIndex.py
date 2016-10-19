from flask_restful import Resource
from . import DataBaseManager, data

parser = data.parser


class DocIndex(Resource):
    @staticmethod
    def get():

        return {'Hello': "world"}
