from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.lqlwz.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

danny = {"first_name": "Danny", "last_name": "Craig", "student_id": "1007"}
trish = {"first_name": "Trish", "last_name": "Trang", "student_id": "1008"}
skadi = {"first_name": "Skadi", "last_name": "Jotun", "student_id": "1009"}

danny_student_id = db.students.insert_one(danny).inserted_id
trish_student_id = db.students.insert_one(trish).inserted_id
skadi_student_id = db.students.insert_one(skadi).inserted_id

print ("-- INSERT STATEMENTS --")
print (danny_student_id)
print (trish_student_id)
print (skadi_student_id)
