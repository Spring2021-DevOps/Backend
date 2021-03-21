from pymongo import MongoClient
from random import randint
import os

myvars = {}
with open(os.path.join("/home/ubuntu/webapp.properties")) as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        myvars[name.strip()] = (str(var)).strip('\n')
    settings.userdata = myvars

client =MongoClient(host=str(settings.userdata['db_host']).strip('\n'), port=27017)
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