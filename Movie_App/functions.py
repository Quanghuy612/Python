from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import io
from db import save_movie, get_all_movies, get_image,update_movie,delete_movie
import tkinter as tk

def upload_image(image_label):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image_data = open(file_path, "rb").read()
        load_image(file_path, image_label)
        return image_data
    return None

def load_image(file_path, image_label):
    image = Image.open(file_path)
    image = image.resize((200, 200))
    img = ImageTk.PhotoImage(image)
    
    image_label.config(image=img)
    image_label.image = img

def save_movie_data(movie_entry, image_data, root, refresh_grid):
    movie_name = movie_entry.get()
    if not movie_name or not image_data:
        messagebox.showerror("Error", "Movie name and image are required!")
        return

    result = save_movie(movie_name, image_data)
    messagebox.showinfo("Success", result)
    movie_entry.delete(0, "end")
    refresh_grid()

def display_movies(frame):
    # Clear the frame before displaying movies
    for widget in frame.winfo_children():
        widget.destroy()

    # Fetch all movies from the database
    movies = get_all_movies()
    row, col = 0, 0
    for movie in movies:
        image_id = movie.get("image_id")
        if image_id:
            # Fetch and display the movie image
            image_data = get_image(image_id)
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((150, 150))
            img = ImageTk.PhotoImage(image)

            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.grid(row=row, column=col, padx=10, pady=10)

            # Bind a click event to the image label
            img_label.bind("<Button-1>", lambda e, movie=movie: open_movie_options(movie, frame))

            # Display the movie name below the image
            name_label = tk.Label(frame, text=movie["name"], bg="#121212", fg="white")
            name_label.grid(row=row + 1, column=col, pady=5)

            col += 1
            if col >= 3:  # Display 3 movies per row
                col = 0
                row += 2

def open_movie_options(movie, frame):
    # Create a new window for movie options
    options_window = tk.Toplevel()
    options_window.title("Movie Options")
    options_window.geometry("600x350")

    # Update Button
    update_button = tk.Button(options_window, text="Update Movie", command=lambda: update_movie_window(movie, options_window, frame))
    update_button.pack(pady=10)

    # Delete Button
    delete_button = tk.Button(options_window, text="Delete Movie", command=lambda: delete_movie_confirmation(movie, options_window, frame))
    delete_button.pack(pady=10)

def update_movie_window(movie, options_window, frame):
    # Create a new window for updating the movie
    update_window = tk.Toplevel(options_window)
    update_window.title("Update Movie")
    update_window.geometry("400x200")

    # Movie Name Entry
    tk.Label(update_window, text="New Movie Name:").pack(pady=10)
    new_name_entry = tk.Entry(update_window, width=30)
    new_name_entry.pack(pady=10)

    # Update Button
    update_button = tk.Button(update_window, text="Update", command=lambda: update_movie(movie, new_name_entry.get(), update_window, frame))
    update_button.pack(pady=10)

def delete_movie_confirmation(movie, options_window, frame):
    # Confirm deletion
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this movie?")
    if confirm:
        delete_movie(movie["id"])  # Delete the movie from the database
        messagebox.showinfo("Success", "Movie deleted successfully!")
        options_window.destroy()
        display_movies(frame)
    # Confirm deletion
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this movie?")
    if confirm:
        delete_movie(movie["id"])
        messagebox.showinfo("Success", "Movie deleted successfully!")
        options_window.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

    movies = get_all_movies()
    row, col = 0, 0
    for movie in movies:
        image_id = movie.get("image_id")
        if image_id:
            image_data = get_image(image_id)
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((150, 150))
            img = ImageTk.PhotoImage(image)

            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.grid(row=row, column=col, padx=10, pady=10)

            name_label = tk.Label(frame, text=movie["name"])
            name_label.grid(row=row+1, column=col, pady=5)

            col += 1
            if col >= 3:
                col = 0
                row += 2 
