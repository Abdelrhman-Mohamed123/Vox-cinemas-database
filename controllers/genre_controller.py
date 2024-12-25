from bson.objectid import ObjectId
from models.genre_model import Genre  # Assuming Genre model is in genre_model.py
from config import genres_collection  # Import the collection from your config file

# Create a new genre
def create_genre(name, description=None):
    new_genre = Genre(
        name=name,
        description=description or ""
    )
    genre_dict = new_genre.to_dict()
    result = genres_collection.insert_one(genre_dict)
    return {"message": "Genre created successfully", "genre_id": str(result.inserted_id)}

# Retrieve all genres
def get_genres():
    genres = genres_collection.find()
    genre_list = []
    for genre in genres:
        genre['_id'] = str(genre['_id'])  # Convert ObjectId to string
        genre_list.append(genre)
    return genre_list

# Retrieve a single genre by ID
def get_genre(genre_id):
    genre = genres_collection.find_one({"_id": ObjectId(genre_id)})
    if not genre:
        return {"error": "Genre not found"}
    genre['_id'] = str(genre['_id'])  # Convert ObjectId to string
    return genre

# Update a genre
def update_genre(genre_id, name=None, description=None):
    updated_data = {}
    if name is not None:
        updated_data['name'] = name
    if description is not None:
        updated_data['description'] = description

    result = genres_collection.update_one({"_id": ObjectId(genre_id)}, {"$set": updated_data})
    if result.matched_count == 0:
        return {"error": "Genre not found"}
    return {"message": "Genre updated successfully"}

# Delete a genre
def delete_genre(genre_id):
    result = genres_collection.delete_one({"_id": ObjectId(genre_id)})
    if result.deleted_count == 0:
        return {"error": "Genre not found"}
    return {"message": "Genre deleted successfully"}