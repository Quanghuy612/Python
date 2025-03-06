# Danh sách công việc (dùng list chứa tuple)
tasks = []

# Thêm công việc vào danh sách
def add_task():
    name = input("Nhập tên công việc: ")
    priority = int(input("Nhập mức độ ưu tiên (số nhỏ hơn nghĩa là ưu tiên cao hơn): "))
    tasks.append((name, priority))
    print(f"Đã thêm công việc: {name} - Ưu tiên {priority}")

# Sắp xếp danh sách công việc theo mức độ ưu tiên
def sort_tasks():
    if not tasks:
        print("Danh sách công việc trống!")
        return

    tasks.sort(key=lambda x: x[1])  # Sắp xếp theo mức độ ưu tiên (số nhỏ hơn ưu tiên hơn)
    print("\nDanh sách công việc sau khi sắp xếp:")
    for index, (name, priority) in enumerate(tasks, start=1):
        print(f"{index}. {name} - Ưu tiên {priority}")

# Chương trình chính
while True:
    print("\n1. Thêm công việc\n2. Sắp xếp và hiển thị công việc\n3. Thoát")
    choice = input("Chọn thao tác (1-3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        sort_tasks()
    elif choice == "3":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
