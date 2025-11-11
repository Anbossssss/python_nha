import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Tạo kết nối đến MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='qlithuoc'
        )
        if connection.is_connected():
            print(" Kết nối MySQL thành công!")
            return connection
    except Error as e:
        print(" Lỗi khi kết nối MySQL:", e)
        return None
