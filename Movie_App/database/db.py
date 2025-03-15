from pymongo import MongoClient
import gridfs

client = MongoClient("mongodb://localhost:27017/")
db = client["movie_database"]
fs = gridfs.GridFS(db)
collection = db["movies"]
users_collection = db["users"]

def verify_user(username, password):
    """Check if the user exists and password matches"""
    user = users_collection.find_one({"username": username, "password": password})
    return user is not None

def save_movie(movie_name, image_data):
    if not movie_name or not image_data:
        return "Movie name and image are required!"
    
    image_id = fs.put(image_data, filename=f"{movie_name}.jpg")
    
    movie_data = {"name": movie_name, "image_id": image_id}
    collection.insert_one(movie_data)
    
    return "Movie saved successfully!"

def get_all_movies():
    return list(collection.find())

def get_image(image_id):
    grid_out = fs.get(image_id)
    return grid_out.read()

def update_movie(movie_id, new_name=None, new_image_data=None):
    try:
        # Find the movie document
        movie = collection.find_one({"_id": movie_id})
        if not movie:
            return "Movie not found!"

        # Update the movie name if provided
        update_data = {}
        if new_name:
            update_data["name"] = new_name

        # Update the movie document in the collection
        if update_data:
            collection.update_one({"_id": movie_id}, {"$set": update_data})
            return "Movie updated successfully!"
        else:
            return "No updates provided!"
    except Exception as e:
        return f"An error occurred while updating the movie: {e}"

def delete_movie(movie_id):
    try:
        # Find the movie document
        movie = collection.find_one({"_id": movie_id})
        if not movie:
            return "Movie not found!"

        # Delete the associated image from GridFS
        if "image_id" in movie:
            fs.delete(movie["image_id"])

        # Delete the movie document from the collection
        collection.delete_one({"_id": movie_id})

        return "Movie deleted successfully!"
    except Exception as e:
        return f"An error occurred while deleting the movie: {e}"