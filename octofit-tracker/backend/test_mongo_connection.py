from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    print("Successfully connected to MongoDB")
    print("Collections:", db.list_collection_names())
except Exception as e:
    print("Error connecting to MongoDB:", e)
