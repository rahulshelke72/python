import pymongo
from pymongo import MongoClient

# Connect to MongoDB
connection_string = "mongodb+srv://james:james3443@cluster0.ygj0etr.mongodb.net/dbinfo?retryWrites=true&w=majority"

client = MongoClient(connection_string)

db = client["dbinfo"]


collection = db["customer"]


records = [
    {"name": "John Doe", "cust_id": 1, "doj": "2022-01-01", "address": "123 Main St", "email": "john@example.com", "mobileno": "1234567890", "experience": 5},
    {"name": "Jane Smith", "cust_id": 2, "doj": "2020-03-01", "address": "456 Elm St", "email": "jane@example.com", "mobileno": "9876543210", "experience": 3},
    {"name": "Ajay", "cust_id": 3, "doj": "20219-02-01", "address": "Pune", "email": "jane@example.com", "mobileno": "9876543211", "experience": 2},
    {"name": "Akash", "cust_id": 4, "doj": "2018-02-01", "address": "PCMc", "email": "jane@example.com", "mobileno": "9876543212", "experience": 4},
    {"name": "Sumit", "cust_id": 5, "doj": "2017-02-01", "address": "Mumbai", "email": "jane@example.com", "mobileno": "9876543213", "experience": 2},
    {"name": "vijay", "cust_id": 6, "doj": "2016-02-01", "address": "nashik", "email": "jane@example.com", "mobileno": "9876543214", "experience": 8},
    {"name": "aman", "cust_id": 7, "doj": "2015-02-01", "address": "banglore", "email": "jane@example.com", "mobileno": "9876543215", "experience": 9},
    {"name": "sujit", "cust_id": 8, "doj": "2014-02-01", "address": "pimpri", "email": "jane@example.com", "mobileno": "9876543216", "experience": 10},
    {"name": "prajwal", "cust_id": 9, "doj": "2013-02-01", "address": "nagar", "email": "jane@example.com", "mobileno": "9876543217", "experience": 12},
    {"name": "shantanu", "cust_id": 10, "doj": "2012-02-01", "address": "PCMC", "email": "jane@example.com", "mobileno": "9876543218", "experience": 11}
]

collection.insert_many(records)
print("Inserted", len(records), "records")


all_records = collection.find()
print("All records:")
for record in all_records:
    print(record)


name_to_search = "John Doe"
search_result = collection.find_one({"name": name_to_search})
print(f"Record for {name_to_search}:")
print(search_result)


cust_id_to_delete = 1
delete_result = collection.delete_one({"cust_id": cust_id_to_delete})
print(f"Deleted {delete_result.deleted_count} record(s)")
