import tkinter as tk
from functions import upload_image, save_movie_data, display_movies

def create_layout(root):
    root.title("Movie App")
    root.geometry("1920x1080")
    root.configure(bg="#121212")

    # Header Frame
    header_frame = tk.Frame(root, bg="#E50914", height=60)
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="Movie Collection", font=("Arial", 20, "bold"), fg="white", bg="#E50914")
    title_label.pack(pady=10)

    # Main Content Frame
    content_frame = tk.Frame(root, bg="#121212")
    content_frame.pack(pady=20)

    # Input and Buttons Container (To align them in one row)
    input_frame = tk.Frame(content_frame, bg="#121212")
    input_frame.pack(pady=10)

    # Movie Name Entry and Label
    tk.Label(input_frame, text="Enter Movie Name:", font=("Arial", 14, "bold"), fg="white", bg="#121212").grid(row=0, column=0, padx=5, pady=5)
    movie_name_entry = tk.Entry(input_frame, width=30, font=("Arial", 14), bd=2, relief="groove")
    movie_name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Upload Image Button
    upload_button = tk.Button(input_frame, text="Upload Image", bg="#1be36e", fg="white")
    upload_button.grid(row=0, column=2, padx=5, pady=5)

    # Save Button
    save_button = tk.Button(input_frame, text="Save Movie", bg="#1c62ed")
    save_button.grid(row=0, column=3, padx=5, pady=5)

    # Image Display Label (Hidden Initially)
    image_label = tk.Label(content_frame)
    image_label.pack(pady=10)
    image_label.pack_forget()  # Hide it initially

    # Frame to hold movie images (grid layout)
    movie_frame = tk.Frame(content_frame, bg="#121212")
    movie_frame.pack(pady=20)

    # Store the uploaded image data
    image_data = {"data": None}

    # Attach functions to buttons
    def upload_and_show_image():
        img = upload_image(image_label)
        if img:
            image_data["data"] = img

    upload_button.config(command=upload_and_show_image)
    save_button.config(command=lambda: save_movie_data(movie_name_entry, image_data["data"], root, lambda: display_movies(movie_frame)))

    # Load existing movies
    display_movies(movie_frame)

    return movie_name_entry, image_label
