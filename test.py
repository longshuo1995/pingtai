from pymongo import MongoClient


client = MongoClient('127.0.0.1', 27017)
db = client.test


r = db.test.insert_one({'name': {1, 2, 3}})
# print(r)

r = db.test.find({})
for i in r:
    print(i)
