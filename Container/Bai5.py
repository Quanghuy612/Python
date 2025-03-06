# Nhập đoạn văn từ người dùng
text = input("Nhập đoạn văn: ")

# Chuẩn hóa văn bản: Chuyển thành chữ thường và loại bỏ dấu câu
import string
text = text.lower().translate(str.maketrans("", "", string.punctuation))

# Tách từ thành danh sách
words = text.split()

# Tạo dictionary để đếm số lần xuất hiện của từng từ
word_count = {}

# Đếm số lần xuất hiện của từng từ
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Hiển thị kết quả
print("\nSố lần xuất hiện của từng từ:")
for word, count in word_count.items():
    print(f"{word}: {count}")
