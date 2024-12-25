from bson.objectid import ObjectId
from models.user_model import User
from config import users_collection  # Importing the database connection

# Create a new user
def create_user(name, gmail, watched_movies=None, favourite_genres=None):
    new_user = User(
        name=name,
        gmail=gmail,
        watched_movies=watched_movies or [],
        favourite_genres=favourite_genres or []
    )
    user_dict = new_user.to_dict()
    result = users_collection.insert_one(user_dict)
    return {"message": "User created successfully", "user_id": str(result.inserted_id)}

# Retrieve all users
def get_users():
    users = users_collection.find()
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
        user_list.append(user)
    return user_list

# Retrieve a single user by ID
def get_user(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        return {"error": "User not found"}
    user['_id'] = str(user['_id'])  # Convert ObjectId to string
    return user

# Update a user
def update_user(user_id, name=None, gmail=None, watched_movies=None, favourite_genres=None):
    updated_data = {}
    if name is not None:
        updated_data['name'] = name
    if gmail is not None:
        updated_data['gmail'] = gmail
    if watched_movies is not None:
        updated_data['watched_movies'] = watched_movies
    if favourite_genres is not None:
        updated_data['favourite_genres'] = favourite_genres

    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_data})
    if result.matched_count == 0:
        return {"error": "User not found"}
    return {"message": "User updated successfully"}

# Delete a user
def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        return {"error": "User not found"}
    return {"message": "User deleted successfully"}
