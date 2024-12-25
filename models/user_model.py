class User:
    def __init__(self, name, gmail, watched_movies=None, favourite_genres=None, user_id=None):
        self.id = user_id  # MongoDB will assign this if it's a new user
        self.name = name
        self.gmail = gmail
        self.watched_movies = watched_movies if watched_movies else []
        self.favourite_genres = favourite_genres if favourite_genres else []

    def to_dict(self):
        return {
            'name': self.name,
            'gmail': self.gmail,
            'watched_movies': self.watched_movies,
            'favourite_genres': self.favourite_genres
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get('name'),
            gmail=data.get('gmail'),
            watched_movies=data.get('watched_movies', []),
            favourite_genres=data.get('favourite_genres', []),
            user_id=data.get('_id')
        )
