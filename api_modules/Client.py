from flask_restful import Resource
from . import DataBaseManager, data

parser = data.parser


class Client(Resource):
    states = ['Prospect', 'Projet en cours', 'Projet terminé', 'Partenaire']

    @staticmethod
    def get():
        connection = DataBaseManager.DataBaseManager.connect()
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('value', type=str, required=True)
        args = parser.parse_args()
        if args['type'] not in ['firstname', 'lastname', 'height', 'town']:
            return {'error': "Type " + args['type'] + " not found"}
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `user` WHERE `" + args['type'] + "`=%s"
                cursor.execute(sql, (args['value']))
                result = cursor.fetchone()
        finally:
            connection.close()

        return {'result': result}

    @staticmethod
    def post():
        connection = DataBaseManager.DataBaseManager.connect()
        parser.add_argument('fullname', type=str, required=True)
        parser.add_argument('enterprise', type=str, required=True)
        parser.add_argument('state', type=str, required=True)
        args = parser.parse_args()
        print(args)
        try:
            with connection.cursor() as cursor:

                if args['state'] not in Client.states:
                    return {'result': 'User state not valid'}

                fullname = args['fullname'].split(" ")
                request = "INSERT INTO `user` (`firstname`, `lastname`, `enterprise`, `state`) VALUES (%s, %s, %s, %s)"
                cursor.execute(request, (fullname[0], fullname[1], args['enterprise'], args["state"]))

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()
        finally:
            connection.close()

        return {'result': "User added"}
