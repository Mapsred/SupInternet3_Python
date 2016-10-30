from flask_restful import Resource
from . import DataBaseManager, data
from flask import request

parser = data.parser


class Client(Resource):
    states = ['Prospect', 'Projet en cours', 'Projet terminé', 'Partenaire']

    @staticmethod
    def get(fullname):

        connection = DataBaseManager.DataBaseManager.connect()
        try:
            with connection.cursor() as cursor:
                name = fullname.split(" ")
                query = "SELECT * FROM `user` WHERE `firstname` = %s AND `lastname` = %s " \
                        "OR `enterprise` = %s OR `state` = %s"
                cursor.execute(query, (name[0], name[1], fullname, fullname))
                result = cursor.fetchone()
        finally:
            connection.close()

        return {'result': result}

    @staticmethod
    def delete(fullname):
        connection = DataBaseManager.DataBaseManager.connect()
        try:
            with connection.cursor() as cursor:

                fullname = fullname.split(" ")
                query = "DELETE FROM `user` WHERE `firstname` = %s AND `lastname` = %s"
                cursor.execute(query, (fullname[0], fullname[1]))

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()
        finally:
            connection.close()

        return {'result': "User deleted"}

    @staticmethod
    def put(fullname):
        connection = DataBaseManager.DataBaseManager.connect()
        parser.add_argument('index', type=str, required=True)
        parser.add_argument('value', type=str, required=True)
        args = parser.parse_args()
        try:
            with connection.cursor() as cursor:

                fullname = fullname.split(" ")
                query = "UPDATE `user` SET `" + args['index'] + "` = %s WHERE `firstname` = %s AND `lastname` = %s"
                cursor.execute(query, (args['value'], fullname[0], fullname[1]))

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()
        finally:
            connection.close()

        return {'result': "User updated"}


class ClientPost(Resource):
    fields = ['fullname', 'lastname', 'firstname', 'enterprise', 'state']

    @staticmethod
    def post():
        connection = DataBaseManager.DataBaseManager.connect()
        parser.add_argument('fullname', type=str, required=True)
        parser.add_argument('enterprise', type=str, required=True)
        args = parser.parse_args()
        try:
            with connection.cursor() as cursor:
                fullname = args['fullname'].split(" ")
                query = "INSERT INTO `user` (`firstname`, `lastname`, `enterprise`, `state`) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (fullname[0], fullname[1], args['enterprise'], "Prospect"))

            # connection is not autocommit by default. So you must commit to save your changes.
            connection.commit()
        finally:
            connection.close()

        return {'result': "User added"}

    @staticmethod
    def get():
        connection = DataBaseManager.DataBaseManager.connect()
        params = request.args.to_dict()
        arguments = []
        for (key, value) in params.items():
            if key not in ClientPost.fields:
                return {'error': "invalid field"}
            else:
                if key == "fullname":
                    arguments.append("firstname")
                    arguments.append("lastname")
                else:
                    arguments.append(key)

        try:
            with connection.cursor() as cursor:
                if "fullname" in params.items():
                    fullname = params['fullname'].split(" ")
                    params['firstname'] = fullname[0]
                    params['lastname'] = fullname[1]
                    del params['fullname']

                query = "SELECT * FROM `user` WHERE"
                queries = []
                for (key, value) in params.items():
                    queries.append(str("`{}` = %s".format(key)))

                query += " AND ".join(queries)
                args = [params[i] for i in arguments]
                cursor.execute(query, args)
                result = cursor.fetchall()
        finally:
            connection.close()

        return {'result': result}
