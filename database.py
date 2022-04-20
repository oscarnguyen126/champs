import pymysql.cursors

class Database:
    def __init__(self):
        self.connection = None

    def get_all_champion(self, sqlString):
        self.connection = pymysql.connect(host='localhost', user='root', password='123456a@',
                                          database='champs', cursorclass=pymysql.cursors.DictCursor)
        cursor = self.connection.cursor()
        cursor.execute(sqlString)
        return cursor.fetchall()
    