import tkinter as tk
from PIL import Image, ImageTk

# Danh sách ảnh và tên sản phẩm
image_data = [
    ("Images/img_1.jpg", "Apple"),
    ("Images/img_2.jpg", "Banana"),
    ("Images/img_3.jpg", "Cherry"),
    ("Images/img_4.jpg", "Grapes"),
    ("Images/img_5.jpg", "Orange"),
    ("Images/img_6.jpg", "Strawberry")
]

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Customer Services App")
root.configure(bg="#A7E6E2")  # Màu nền xanh nhạt
root.geometry("700x600")

title_label = tk.Label(root, text="🛍️ Welcome to the Shop", font=("Arial", 20, "bold"), bg="#A7E6E2")
title_label.pack(pady=10)

search_frame = tk.Frame(root, bg="#A7E6E2")
search_frame.pack(pady=5)

tk.Label(search_frame, text="🔎 Search:", font=("Arial", 12, "bold"), bg="#A7E6E2").grid(row=0, column=0, padx=5)
search_entry = tk.Entry(search_frame, font=("Arial", 12), width=20)
search_entry.grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="Search", font=("Arial", 12), fg="white", bg="orange").grid(row=0, column=2, padx=5)

image_frame = tk.Frame(root, bg="#A7E6E2")
image_frame.pack(pady=10)

photo_refs = []

for index, (img_path, label_text) in enumerate(image_data):

    try:
        # Mở và xử lý ảnh
        image = Image.open(img_path).resize((250, 250))
        photo = ImageTk.PhotoImage(image)
        photo_refs.append(photo)

        # Tạo frame con để chứa ảnh + nhãn
        frame = tk.Frame(image_frame, bg="white", bd=2, relief="solid")
        frame.grid(row=index // 3, column=index % 3, padx=15, pady=15)

        # Hiển thị ảnh
        img_label = tk.Label(frame, image=photo, bg="white")
        img_label.pack()

        # Hiển thị tên sản phẩm
        text_label = tk.Label(frame, text=label_text, font=("Arial", 12, "bold"), bg="white")
        text_label.pack()

    except Exception as e:
        print(f"❌ Lỗi khi mở ảnh '{img_path}': {e}")

# Chạy giao diện
root.mainloop()
