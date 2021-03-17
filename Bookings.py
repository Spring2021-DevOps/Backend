from flask import Flask, request, jsonify
from bson.objectid import ObjectId
import uuid
import DatabaseOperations as database
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/book-trip', methods=["POST"])
def bookTrip():
    firstName = request.json["firstNameP"]
    lastName = request.json["lastNameP"]
    source = request.json["sourceP"]
    destination = request.json["destinationP"]
    journeyDate = request.json["journeydDateP"]

    booking = dict(firstName=firstName, lastName=lastName, source=source,
                destination=destination, journeyDate=journeyDate,
                _id=str(ObjectId()))
    #database.add_booking(booking)
    return jsonify("Booked new trip")

@app.route('/bookings', methods=["GET"])
def getAllBookings():
    bookings = database.get_bookings()
    return jsonify(bookings)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')