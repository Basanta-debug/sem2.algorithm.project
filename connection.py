import mysql.connector


class MyDb:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
            user='root', host='localhost', password='Basanta@9865', port=3306, database='Project')
        self.my_cursor = self.my_connection.cursor()

    def iud(self, qry, values):
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()

    def get_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data

    def get_data_p(self, qry, values):
        self.my_cursor.execute(qry, values)
        data = self.my_cursor.fetchall()
        return data

