import pymysql.cursors
from . import parameters


class DataBaseManager:
    @staticmethod
    def connect():
        return pymysql.connect(host=parameters.host,
                               user=parameters.user,
                               password=parameters.password,
                               db=parameters.db,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
