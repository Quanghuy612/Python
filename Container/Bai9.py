# Nhập danh sách cặp (tên, điểm) từ người dùng
num_students = int(input("Nhập số lượng học sinh: "))

# Tạo danh sách để lưu các cặp (tên, điểm)
student_list = []

for _ in range(num_students):
    name = input("Nhập tên học sinh: ")
    score = float(input("Nhập điểm số: "))
    student_list.append((name, score)) 

# Chuyển danh sách thành dictionary
student_dict = dict(student_list)

# Hiển thị kết quả
print("\nDanh sách học sinh dưới dạng từ điển:")
print(student_dict)
