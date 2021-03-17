from flask import Flask, request, jsonify
from bson.objectid import ObjectId
import uuid
import DatabaseOperations as database

app = Flask(__name__)


@app.route('/book-trip', methods=["POST"])
def bookTrip():
    firstName = "Divya"#request.json["firstName"]
    lastName = "Girase"#request.json["lastName"]
    source = "Boston"#request.json["source"]
    destination = "NewYork" #request.json["destination"]
    journeyDate = "02-21-2021" #request.json["date"]

    booking = dict(firstName=firstName, lastName=lastName, source=source,
                destination=destination, journeyDate=journeyDate,
                _id=str(ObjectId()))
    database.add_booking(booking)
    return "Booking new trip"

@app.route('/bookings', methods=["GET"])
def getAllBookings():
    bookings = database.get_bookings()
    return jsonify(bookings)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')