from flask_restful import Resource
from . import DataBaseManager, data

parser = data.parser


class GetUser(Resource):
    @staticmethod
    def get():
        connection = DataBaseManager.DataBaseManager.connect()
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('value', type=str, required=True)
        args = parser.parse_args()
        if args['type'] not in ['firstname', 'lastname', 'height', 'town']:
            return {'error': "Type "+args['type']+" not found"}
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `user` WHERE `"+args['type']+"`=%s"
                cursor.execute(sql, (args['value']))
                result = cursor.fetchone()
        finally:
            connection.close()

        return {'result': result}

