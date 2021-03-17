from pymongo import MongoClient
from random import randint

client =MongoClient(host="3.89.160.125", port=27017)
db=client.Uber

def add_booking(booking):
    print("Adding booking to database!")
    bookingId = None
    try:
        result = db.bookings.insert_one(booking)
        print("Booking added to database..")
        bookingId = result.inserted_id
    except Exception as e:
        print("Booking new trip: An exception occurred: ", e)
    return bookingId

def get_bookings():
    print("Getting all bookings from database!")
    try:
        bookingsList = []
        result = db.bookings.find().sort("journeyDate")
        for booking in result:
            bookingsList.append(booking)
        print("Fetched all bookings from database..")
        return bookingsList
    except Exception as e:
        print("Getting all bookings: An exception occurred: ", e)
    return None