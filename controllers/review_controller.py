from bson.objectid import ObjectId
from bson.errors import InvalidId  # Import InvalidId exception
from models.review_model import Review  # Assuming Review model is in review_model.py
from config import reviews_collection, movies_collection, users_collection  # Import the collections from your config file

# Create a new review
def create_review(movie_id, user_id, review_rating):
    # Validate the movie ID format
    try:
        movie_object_id = ObjectId(movie_id)  # Convert to ObjectId if valid
    except InvalidId:
        return {"error": f"'{movie_id}' is not a valid ObjectId. Please provide a valid movie ID."}

    # Validate the user ID format
    try:
        user_object_id = ObjectId(user_id)  # Convert to ObjectId if valid
    except InvalidId:
        return {"error": f"'{user_id}' is not a valid ObjectId. Please provide a valid user ID."}

    # Check if the movie ID exists in the movies collection
    if not movies_collection.find_one({"_id": movie_object_id}):
        return {"error": "Movie ID does not exist in the movies collection"}

    # Check if the user ID exists in the users collection
    if not users_collection.find_one({"_id": user_object_id}):
        return {"error": "User ID does not exist in the users collection"}

    # Check if a review for this movie ID already exists
    if reviews_collection.find_one({"movie_id": movie_id, "user_id": user_id}):
        return {"error": "A review for this movie by this user already exists"}

    new_review = Review(movie_id=movie_id, user_id=user_id, review_rating=review_rating)
    review_dict = new_review.to_dict()
    result = reviews_collection.insert_one(review_dict)
    return {"message": "Review created successfully", "review_id": str(result.inserted_id)}

# Retrieve all reviews
def get_reviews():
    reviews = reviews_collection.find()
    review_list = []
    for review in reviews:
        review['_id'] = str(review['_id'])  # Convert ObjectId to string
        review_list.append(review)
    return review_list

# Retrieve reviews for a specific movie
def get_reviews_by_movie(movie_id):
    reviews = reviews_collection.find({"movie_id": movie_id})
    review_list = []
    for review in reviews:
        review['_id'] = str(review['_id'])  # Convert ObjectId to string
        review_list.append(review)
    return review_list

# Retrieve a single review by ID
def get_review(review_id):
    review = reviews_collection.find_one({"_id": ObjectId(review_id)})
    if not review:
        return {"error": "Review not found"}
    review['_id'] = str(review['_id'])  # Convert ObjectId to string
    return review

# Update a review
def update_review(review_id, review_rating=None):
    updated_data = {}
    if review_rating is not None:
        updated_data['review_rating'] = review_rating

    result = reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$set": updated_data})
    if result.matched_count == 0:
        return {"error": "Review not found"}
    return {"message": "Review updated successfully"}

# Delete a review
def delete_review(review_id):
    result = reviews_collection.delete_one({"_id": ObjectId(review_id)})
    if result.deleted_count == 0:
        return {"error": "Review not found"}
    return {"message": "Review deleted successfully"}