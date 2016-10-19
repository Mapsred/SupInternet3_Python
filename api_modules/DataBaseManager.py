import pymysql.cursors


class DataBaseManager:
    @staticmethod
    def connect():
        return pymysql.connect(host='localhost',
                               user='maps_red',
                               password='lOTarInT',
                               db='python_api',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
