from bson import ObjectId

class Review:
    def __init__(self, movie_id, user_id, review_rating, review_id=None):
        self.id = review_id  # Will be assigned by MongoDB if it's a new review
        self.movie_id = movie_id  # The ID of the movie being reviewed
        self.user_id = user_id  # The ID of the user who wrote the review
        self.review_rating = review_rating  # The rating given by the user

    def to_dict(self):
        """Convert the review model to a dictionary for saving into MongoDB"""
        return {
            'movie_id': self.movie_id,
            'user_id': self.user_id,
            'review_rating': self.review_rating
        }