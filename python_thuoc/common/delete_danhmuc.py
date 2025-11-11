from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

# 🗑️ Hàm xóa danh mục theo ID
def delete_danhmuc(madm):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "DELETE FROM danhmuc WHERE madm = %s"
        cursor.execute(sql, (madm,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f" Đã xóa danh mục có ID = {madm}")
        else:
            print(" Không tìm thấy danh mục để xóa.")
    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Đã đóng kết nối MySQL.")
