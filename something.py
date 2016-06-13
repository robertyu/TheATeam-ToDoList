from pymongo import MongoClient
import pprint


client = MongoClient()
tesla_s = {
        'manufacturer':'Tesla Motors',
        'class' : 'full-size'
    }

db = client.examples
db.autos.insert(tesla_s)

for a in db.autos.find():
    print (a)
