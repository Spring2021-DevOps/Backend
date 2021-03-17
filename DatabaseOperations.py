from pymongo import MongoClient
from random import randint

client =MongoClient(host="3.94.170.170", port=27017)
db=client.Uber

def add_booking(booking):
    print(booking)
    try:
        result = db.bookings.insert_one(booking)
        print(result.inserted_id)
    except Exception as e:
        print(e)

def get_bookings():
    try:
        result = db.bookings.find().sort("journeyDate")
        return result
    except Exception as e:
        print(e)