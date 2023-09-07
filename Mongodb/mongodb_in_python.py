import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient('localhost', 27017)

# Select an existing database or create a new one
db = client['mydatabase']

# Select an existing collection or create a new one
collection = db['mycollection']

# Insert a document into the collection
data = {'name': 'John', 'age': 30}
result = collection.insert_one(data)

# Find a document in the collection
query = {'name': 'John'}
document = collection.find_one(query)

# Print the found document
print(document)

# Close the connection
client.close()
