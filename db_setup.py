import mysql.connector

mysql_db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='snappfood'
)

my_cursor = mysql_db.cursor()
my_cursor.execute('select * from user_1')
users = my_cursor.fetchall()
print(users)
