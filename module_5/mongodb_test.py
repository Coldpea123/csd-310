#Andy Nguyen
#6/19/2022
#Module 5

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.lqlwz.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())
