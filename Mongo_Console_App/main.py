import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

# GUI Application
root = tk.Tk()
root.title("Quản Lý Người Dùng")
root.geometry("600x400")

# === Functions ===
def display_users():
    """Load user data from MongoDB and display it in the table."""
    for row in tree.get_children():
        tree.delete(row)  # Clear table before updating

    users = collection.find()
    for user in users:
        user_id = user.get("_id", "N/A")
        name = user.get("name", "N/A")
        age = user.get("age", "N/A")  # Avoid KeyError
        email = user.get("email", "N/A")
        tree.insert("", "end", values=(user_id, name, age, email))

def add_user():
    """Insert a new user into MongoDB."""
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()

    if not name or not age or not email:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        age = int(age)  # Ensure age is an integer
    except ValueError:
        messagebox.showerror("Lỗi", "Tuổi phải là số nguyên!")
        return

    user = {"name": name, "age": age, "email": email}
    collection.insert_one(user)

    messagebox.showinfo("Thành công", "Người dùng đã được thêm!")
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    display_users()

def update_user():
    """Update the selected user's details in MongoDB."""

    email = entry_email.get().strip()
    new_name = entry_name.get().strip()
    new_age = entry_age.get().strip()

    if not email:
        messagebox.showwarning("Lỗi", "Nhập email của người dùng cần cập nhật!")
        return

    update_data = {}
    if new_name:
        update_data["name"] = new_name
    if new_age:
        try:
            update_data["age"] = int(new_age)
        except ValueError:
            messagebox.showerror("Lỗi", "Tuổi phải là số nguyên!")
            return

    if update_data:
        result = collection.update_one({"email": email}, {"$set": update_data})
        if result.modified_count > 0:
            messagebox.showinfo("Thành công", "Cập nhật thành công!")
        else:
            messagebox.showwarning("Lỗi", "Không tìm thấy người dùng hoặc không có thay đổi.")
    display_users()

def delete_user():
    """Delete the selected user from MongoDB."""

    email = entry_email.get().strip()
    if not email:
        messagebox.showwarning("Lỗi", "Nhập email của người dùng cần xóa!")
        return

    result = collection.delete_one({"email": email})
    if result.deleted_count > 0:
        messagebox.showinfo("Thành công", "Người dùng đã được xóa!")
    else:
        messagebox.showwarning("Lỗi", "Không tìm thấy người dùng!")
    
    display_users()

# === UI Layout ===
frame = tk.Frame(root)
frame.pack(pady=10)

# Labels and Entry Fields
tk.Label(frame, text="Tên:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Tuổi:").grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(frame)
entry_age.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Thêm", command=add_user)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(button_frame, text="Cập nhật", command=update_user)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(button_frame, text="Xóa", command=delete_user)
btn_delete.grid(row=0, column=2, padx=5)

# Table (Treeview)
columns = ("ID", "Tên", "Tuổi", "Email")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(pady=10)

# Load Data Initially
display_users()

# Run the Application
root.mainloop()
