from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhập vào tên danh mục: ")
    mota = input("Nhập vào mô tả: ")
    insert_danhmuc(ten, mota)

    con = input("TIẾP TỤC (y), THOÁT thì nhập ký tự bất kỳ: ")
    if con.lower() != "y":
        break
