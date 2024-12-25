from pymongo import MongoClient

# MongoDB Configuration
MONGO_URI = "mongodb+srv://bodebob899:ES3LIicTwjkvsmol@cluster0.mpfdl.mongodb.net/"
DATABASE_NAME = "vox_cinema"

# Establish a connection to MongoDB
client = MongoClient(MONGO_URI)

# Access the database
db = client[DATABASE_NAME]

# Collections
users_collection = db['users']
movies_collection = db['movies']
reviews_collection = db['reviews']
genres_collection = db['genres']