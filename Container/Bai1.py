# Danh sách nhân viên (list)
employees = []

# Thêm nhân viên
def add_employee():
    name = input("Nhập tên nhân viên cần thêm: ")
    employees.append(name)
    print(f"Đã thêm nhân viên: {name}")

# Xóa nhân viên
def remove_employee():
    name = input("Nhập tên nhân viên cần xóa: ")
    if name in employees:
        employees.remove(name)
        print(f"Đã xóa nhân viên: {name}")
    else:
        print(f"Không tìm thấy nhân viên: {name}")

# Hiển thị danh sách nhân viên
def list_employees():
    if employees:
        print("Danh sách nhân viên:", employees)
    else:
        print("Danh sách nhân viên trống.")

# Chạy chương trình
while True:
    print("\n1. Thêm nhân viên\n2. Xóa nhân viên\n3. Hiển thị danh sách\n4. Thoát")
    choice = input("Chọn thao tác (1-4): ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        remove_employee()
    elif choice == "3":
        list_employees()
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
