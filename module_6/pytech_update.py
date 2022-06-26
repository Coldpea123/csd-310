from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.lqlwz.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

i4 = db.students.find({},{"_id": 0})

print("-- DISPLAYING STUDENTS FROM DOCUMENTS FROM find() QUERY --")
for doc1 in i4:
    print(doc1)

result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Carter"}})

print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() QUERY --")
print(db.students.find_one({"student_id": "1007"}, {"_id": 0}))
