from bson import ObjectId

class Movie:
    def __init__(self, title, genre, release_year, ratings=None, movie_id=None):
        self.id = movie_id  # Will be assigned by MongoDB if it's a new movie
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.ratings = ratings if ratings else 0.0  # Default rating is 0.0

    def to_dict(self):
        """Convert the movie model to a dictionary for saving into MongoDB"""
        return {
            'title': self.title,
            'genre': self.genre,
            'release_year': self.release_year,
            'ratings': self.ratings
        }