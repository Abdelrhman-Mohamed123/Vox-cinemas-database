from bson import ObjectId

class Genre:
    def __init__(self, name, description=None, genre_id=None):
        self.id = genre_id  # Will be assigned by MongoDB if it's a new genre
        self.name = name  # Name of the genre
        self.description = description if description else ""  # Optional description

    def to_dict(self):
        """Convert the genre model to a dictionary for saving into MongoDB"""
        return {
            'name': self.name,
            'description': self.description
        }