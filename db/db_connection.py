import mysql.connector

db = mysql.connector.connect(host="localhost", port=3307, user='root', password='1234',
                             database='fb_selenium_screen_shot_py')

if db:
    print('connected')
else:
    print('connection fail')


def get_db_connection():
    return db
