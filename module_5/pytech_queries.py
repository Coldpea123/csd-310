from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.lqlwz.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

print("-- STUDENTS FROM find() QUERY --")
for doc in docs:
    print(doc)

doc2 = db.students.find_one({"student_id": "1009"})

print("-- STUDENT FROM fine_one() QUERY --")
print(doc2)
