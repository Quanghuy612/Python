# Nhập danh sách sản phẩm đã bán (cách nhau bởi dấu phẩy)
sold_products = input("Nhập danh sách sản phẩm đã bán (cách nhau bằng dấu phẩy): ")

# Chuyển chuỗi thành danh sách
product_list = sold_products.split(",")

# Tạo dictionary để đếm số lượng từng sản phẩm
product_count = {}

# Đếm số lần xuất hiện của từng sản phẩm
for product in product_list:
    product = product.strip()
    product_count[product] = product_count.get(product, 0) + 1

# Hiển thị kết quả
print("\nSố lượng sản phẩm đã bán:")
for product, count in product_count.items():
    print(f"{product}: {count} cái")
