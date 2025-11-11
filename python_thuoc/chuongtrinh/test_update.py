from common.update_danhmuc import update_danhmuc  # nhớ import đúng file

while True:
    madm = input("Mã danh mục: ")
    ten = input("Nhập vào tên danh mục: ")
    mota = input("Nhập vào mô tả: ")
    update_danhmuc(madm, ten, mota)

    con = input("TIẾP TỤC (y), THOÁT thì nhập ký tự bất kỳ: ")
    if con.lower() != "y":
        break
