from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()
connection_url = os.getenv('MONGO_URL')
db = MongoClient(connection_url)
print(db.auth.users.find())
try:
    db.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)