import os
import dotenv
from pymongo import MongoClient
dotenv.load_dotenv()

DBURL = os.getenv('URL')

client = MongoClient('mongodb://localhost/RickAndMorty')
db = client.get_database()
collection = db.get_collection("frase2")