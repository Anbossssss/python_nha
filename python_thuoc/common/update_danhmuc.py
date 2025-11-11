from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

# 📝 Hàm cập nhật tên và mô tả danh mục theo ID
def update_danhmuc(madm, ten_moi, mota_moi):
    try:
        connection = connect_mysql()
        if connection is None:
            return

        cursor = connection.cursor()
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE madm = %s"
        cursor.execute(sql, (ten_moi, mota_moi, madm))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã cập nhật danh mục có ID = {madm}")
        else:
            print("⚠️ Không tìm thấy danh mục để cập nhật.")
    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Đã đóng kết nối MySQL.")
