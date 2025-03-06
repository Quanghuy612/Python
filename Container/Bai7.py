from collections import deque

# Tạo hàng đợi khách hàng
queue = deque()

# Thêm khách hàng vào hàng đợi
def add_customer():
    name = input("Nhập tên khách hàng: ")
    queue.append(name)
    print(f"Đã thêm khách hàng: {name}")

# Phục vụ khách hàng (lấy khách hàng đầu tiên ra khỏi hàng đợi)
def serve_customer():
    if queue:
        served = queue.popleft()
        print(f"Đã phục vụ khách hàng: {served}")
    else:
        print("Không có khách hàng nào trong hàng đợi!")

# Hiển thị danh sách khách hàng trong hàng đợi
def show_queue():
    if queue:
        print("\nDanh sách khách hàng trong hàng đợi:")
        for index, name in enumerate(queue, start=1):
            print(f"{index}. {name}")
    else:
        print("Hàng đợi trống!")

# Chương trình chính
while True:
    print("\n1. Thêm khách hàng\n2. Phục vụ khách hàng\n3. Hiển thị hàng đợi\n4. Thoát")
    choice = input("Chọn thao tác (1-4): ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        serve_customer()
    elif choice == "3":
        show_queue()
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
