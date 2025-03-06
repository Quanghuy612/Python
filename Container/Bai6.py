# Nhập danh sách IP từ log truy cập (có thể nhập nhiều IP, cách nhau bởi dấu phẩy)
log_data = input("Nhập danh sách IP truy cập (cách nhau bằng dấu phẩy): ")

# Chuyển chuỗi thành danh sách IP
ip_list = log_data.split(",")

# Dùng set để lấy các IP duy nhất
unique_ips = set(ip.strip() for ip in ip_list)  # Loại bỏ khoảng trắng thừa

# Hiển thị danh sách IP duy nhất
print("\nDanh sách IP duy nhất:")
for ip in unique_ips:
    print(ip)
