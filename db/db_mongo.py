from pymongo import MongoClient


client = MongoClient('127.0.0.1', 27017)
account = client.account
print(account)

