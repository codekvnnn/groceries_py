import mysql.connector
connection = None
def get_connection():
    global connection
    if connection is None:
        connection = mysql.connector.connect(user='root', password='Password',
                                      host='127.0.0.1',
                                      database='g_products')
    return connection
