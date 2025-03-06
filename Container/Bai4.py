# Danh sách học sinh (dùng dictionary)
students = {}

# Nhập danh sách học sinh
def add_student():
    name = input("Nhập tên học sinh: ")
    score = float(input("Nhập điểm số: "))
    students[name] = score
    print(f"Đã thêm học sinh: {name} - {score} điểm")

# Sắp xếp danh sách theo điểm giảm dần
def sort_students():
    if not students:
        print("Danh sách trống!")
        return

    sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
    print("Danh sách học sinh sau khi sắp xếp:")
    for index, (name, score) in enumerate(sorted_students, start=1):
        print(f"{index}. {name} - {score} điểm")

# Chương trình chính
while True:
    print("\n1. Thêm học sinh\n2. Sắp xếp danh sách\n3. Thoát")
    choice = input("Chọn thao tác (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        sort_students()
    elif choice == "3":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
