from pymongo import MongoClient 
from PIL import Image, ImageTk 
import random 
import os 

client = MongoClient('mongodb://localhost:27017/') 
db = client['recipe_manager'] 
feedback_collection = db['feedback'] 

categories = [ 
    {"id": 1, "name": "Main Courses"}, 
    {"id": 2, "name": "Desserts"}, 
    {"id": 3, "name": "Appetizers"}, 
    {"id": 4, "name": "Beverages"}, 
] 
recipes = [ 
    {"id": 1, "categoryId": 1, "name": "Spiced Bean Tacos", "ingredients": "Iceberg lettuce, kidney beans, sour cream, jalapeños...", "steps": "Heat oil, add beans, serve in tacos...", "time": "25 min", "serves": "2"}, 
    {"id": 2, "categoryId": 1, "name": "Grilled Chicken", "ingredients": "Chicken, olive oil, garlic, rosemary...", "steps": "Marinate, grill for 20 min...", "time": "30 min", "serves": "4"}, 
    {"id": 3, "categoryId": 1, "name": "Beef Stir-Fry", "ingredients": "Beef, bell peppers, soy sauce...", "steps": "Stir-fry beef and veggies...", "time": "20 min", "serves": "3"}, 
    {"id": 4, "categoryId": 1, "name": "Pasta Primavera", "ingredients": "Pasta, zucchini, tomatoes, cream...", "steps": "Cook pasta, mix with sauce...", "time": "25 min", "serves": "4"}, 
    {"id": 5, "categoryId": 1, "name": "Salmon with Lemon", "ingredients": "Salmon, lemon, butter, herbs...", "steps": "Bake at 180°C for 15 min...", "time": "20 min", "serves": "2"}
]

def save_feedback(recipe_name, feedback_text): 
    feedback_data = {"recipeId": recipe_name, "feedback": feedback_text} 
    feedback_collection.insert_one(feedback_data) 
    
def get_feedbacks(recipe_name): 
    return list(feedback_collection.find({"recipeId": recipe_name})) 

def get_random_image(): 
    image_files = [f"img{i}.jpg" for i in range(1, 5)] 
    image_file = random.choice(image_files) 
    image_path = os.path.join("images", image_file) 
    try: 
        img = Image.open(image_path).resize((400, 300), Image.LANCZOS) 
        return ImageTk.PhotoImage(img) 
    except FileNotFoundError: 
        print(f"Error: Image file {image_path} not found.") 
        return None