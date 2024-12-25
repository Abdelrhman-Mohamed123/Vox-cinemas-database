from bson.objectid import ObjectId
from models.movie_model import Movie  # Assuming Movie model is in movie_model.py
from config import movies_collection  # Import the collection from your config file

# Create a new movie
def create_movie(title, genre, release_year, ratings=None):
    new_movie = Movie(
        title=title,
        genre=genre,
        release_year=release_year,
        ratings=ratings or 0.0
    )
    movie_dict = new_movie.to_dict()
    result = movies_collection.insert_one(movie_dict)
    return {"message": "Movie created successfully", "movie_id": str(result.inserted_id)}

# Retrieve all movies
def get_movies():
    movies = movies_collection.find()
    movie_list = []
    for movie in movies:
        movie['_id'] = str(movie['_id'])  # Convert ObjectId to string
        movie_list.append(movie)
    return movie_list

# Retrieve a single movie by ID
def get_movie(movie_id):
    movie = movies_collection.find_one({"_id": ObjectId(movie_id)})
    if not movie:
        return {"error": "Movie not found"}
    movie['_id'] = str(movie['_id'])  # Convert ObjectId to string
    return movie

# Update a movie
def update_movie(movie_id, title=None, genre=None, release_year=None, ratings=None):
    updated_data = {}
    if title is not None:
        updated_data['title'] = title
    if genre is not None:
        updated_data['genre'] = genre
    if release_year is not None:
        updated_data['release_year'] = release_year
    if ratings is not None:
        updated_data['ratings'] = ratings

    result = movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": updated_data})
    if result.matched_count == 0:
        return {"error": "Movie not found"}
    return {"message": "Movie updated successfully"}

# Delete a movie
def delete_movie(movie_id):
    result = movies_collection.delete_one({"_id": ObjectId(movie_id)})
    if result.deleted_count == 0:
        return {"error": "Movie not found"}
    return {"message": "Movie deleted successfully"}