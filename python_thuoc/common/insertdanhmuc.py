# Hàm thêm 1 danh mục mới
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error

def insert_danhmuc(tendm, mota):
    connection = connect_mysql()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (tendm, mota) VALUES (%s, %s)"
        values = (tendm, mota)
        cursor.execute(sql, values)
        connection.commit()  # lưu thay đổi vào DB
        print(f"✅ Đã thêm danh mục: {tendm}")
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Đã đóng kết nối MySQL.")


