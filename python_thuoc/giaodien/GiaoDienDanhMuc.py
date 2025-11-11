import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error


# 🧩 HÀM KẾT NỐI MYSQL
def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='qlithuoc'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Lỗi kết nối", f"Lỗi MySQL: {e}")
        return None


# ➕ HÀM THÊM DANH MỤC
def insert_danhmuc(madm, tendm, mota):
    try:
        connection = connect_mysql()
        if connection is None:
            return
        cursor = connection.cursor()
        sql = "INSERT INTO danhmuc (madm, tendm, mota) VALUES (%s, %s, %s)"
        cursor.execute(sql, (madm, tendm, mota))
        connection.commit()
        messagebox.showinfo("Thành công", f"Đã thêm danh mục: {tendm}")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm danh mục: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ✏️ HÀM CẬP NHẬT DANH MỤC
def update_danhmuc(madm, tendm, mota):
    try:
        connection = connect_mysql()
        if connection is None:
            return
        cursor = connection.cursor()
        sql = "UPDATE danhmuc SET tendm = %s, mota = %s WHERE madm = %s"
        cursor.execute(sql, (tendm, mota, madm))
        connection.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Thành công", "Đã cập nhật danh mục.")
        else:
            messagebox.showwarning("Thông báo", "Không tìm thấy mã danh mục cần cập nhật.")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi cập nhật danh mục: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# 🗑️ HÀM XÓA DANH MỤC
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
            messagebox.showinfo("Thành công", f"Đã xóa danh mục có mã {madm}")
        else:
            messagebox.showwarning("Thông báo", "Không tìm thấy danh mục cần xóa.")
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa danh mục: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# 📋 HÀM LẤY DANH SÁCH DANH MỤC
def get_all_danhmuc():
    try:
        connection = connect_mysql()
        if connection is None:
            return []
        cursor = connection.cursor()
        sql = "SELECT madm, tendm, mota FROM danhmuc"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lấy danh sách danh mục: {e}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ======================== GIAO DIỆN ========================

root = tk.Tk()
root.title("Quản lý Danh Mục")
root.geometry("700x500")

# Frame nhập liệu
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Mã DM:").grid(row=0, column=0, padx=5)
entry_id = tk.Entry(frame_input, width=10)
entry_id.grid(row=0, column=1)

tk.Label(frame_input, text="Tên DM:").grid(row=0, column=2, padx=5)
entry_ten = tk.Entry(frame_input, width=20)
entry_ten.grid(row=0, column=3)

tk.Label(frame_input, text="Mô tả:").grid(row=0, column=4, padx=5)
entry_mota = tk.Entry(frame_input, width=25)
entry_mota.grid(row=0, column=5)


# ======================== HÀM CHỨC NĂNG GUI ========================

def them_danhmuc():
    madm = entry_id.get()
    tendm = entry_ten.get()
    mota = entry_mota.get()
    if not madm or not tendm:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ Mã và Tên danh mục.")
        return
    insert_danhmuc(madm, tendm, mota)
    load_danhmuc()


def sua_danhmuc():
    madm = entry_id.get()
    tendm = entry_ten.get()
    mota = entry_mota.get()
    if not madm:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã danh mục cần cập nhật.")
        return
    update_danhmuc(madm, tendm, mota)
    load_danhmuc()


def xoa_danhmuc():
    madm = entry_id.get()
    if not madm:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã danh mục cần xóa.")
        return
    delete_danhmuc(madm)
    load_danhmuc()


def load_danhmuc():
    for i in tree.get_children():
        tree.delete(i)
    for row in get_all_danhmuc():
        tree.insert("", "end", values=row)


# Frame nút
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="Thêm", width=10, command=them_danhmuc).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Cập nhật", width=10, command=sua_danhmuc).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Xóa", width=10, command=xoa_danhmuc).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="Hiển thị", width=10, command=load_danhmuc).grid(row=0, column=3, padx=5)


# Bảng hiển thị
columns = ("madm", "tendm", "mota")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("madm", text="Mã DM")
tree.heading("tendm", text="Tên Danh Mục")
tree.heading("mota", text="Mô tả")
tree.pack(fill="both", expand=True, pady=10)


# Tải dữ liệu ban đầu
load_danhmuc()

root.mainloop()
