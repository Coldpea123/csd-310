from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.lqlwz.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

i3 = db.students.find({}, {"_id": 0})

print("-- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY --")
for doc1 in i3:
    print(doc1)

mystudent = {"student_id": "1010", "first_name": "Thomas", "last_name": "Lake"}
myinsert = db.students.insert_one(mystudent)

print("-- INSERT STATEMENTS --")
print(myinsert.inserted_id)

i5 = db.students.find({}, {"_id": 0})

print("-- DISPLAYING NEW STUDENT LIST DOC --")
for doc2 in i5:
    print(doc2)

myquery = {"student_id": "1010"}
db.students.delete_one(myquery)

i7 = db.students.find({}, {"_id": 0})

print("-- DELETED STUDENT ID: 1010 --")
for doc3 in i7:
    print(doc3)