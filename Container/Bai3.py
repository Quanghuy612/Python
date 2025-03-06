# Tạo tập hợp sản phẩm
products = set()

# Thêm sản phẩm
def add_product():
    product = input("Nhập tên sản phẩm cần thêm: ")
    if product in products:
        print(f"Sản phẩm '{product}' đã tồn tại!")
    else:
        products.add(product)
        print(f"Đã thêm sản phẩm: {product}")

# Xóa sản phẩm
def remove_product():
    product = input("Nhập tên sản phẩm cần xóa: ")
    if product in products:
        products.remove(product)
        print(f"Đã xóa sản phẩm: {product}")
    else:
        print(f"Sản phẩm '{product}' không tồn tại!")

# Hiển thị danh sách sản phẩm
def list_products():
    if products:
        print("Danh sách sản phẩm:", products)
    else:
        print("Cửa hàng chưa có sản phẩm nào.")

# Menu lựa chọn
while True:
    print("\n1. Thêm sản phẩm\n2. Xóa sản phẩm\n3. Hiển thị danh sách\n4. Thoát")
    choice = input("Chọn thao tác (1-4): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        list_products()
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
