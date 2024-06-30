import mysql.connector
class Database:
    __connection = mysql.connector.connect(user="root", host="127.0.0.1", port="3306",
                                          password="20232023", database="world", consume_results=True)
    
    __coursor = __connection.cursor(prepared=True)


    @classmethod
    def cursor(cls):
        return cls.__coursor
    