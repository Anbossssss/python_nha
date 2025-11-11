from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def get_all_danhmuc():
    """Lấy tất cả danh mục từ cơ sở dữ liệu."""
    try:
        connection = connect_mysql()
        if connection is None:
            return []  # trả về list rỗng nếu không kết nối được

        cursor = connection.cursor()
        sql = "SELECT madm, tendm, mota FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()

        # In ra console để debug
        if len(result) == 0:
            print("⚠️ Không có danh mục nào trong cơ sở dữ liệu.")
        else:
            print("📋 DANH SÁCH DANH MỤC:")
            print("-" * 50)
            for row in result:
                print(f" ID: {row[0]} |  Tên: {row[1]} |  Mô tả: {row[2]}")

        return result  # ⚠️ Quan trọng: trả về kết quả để GUI hiển thị

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("✅ Đã đóng kết nối MySQL.")
