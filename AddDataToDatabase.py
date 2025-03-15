import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate("newkey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-2a881-default-rtdb.asia-southeast1.firebasedatabase.app/",
})

# Reference the 'Students' node
ref = db.reference('Students')

# Data with phone numbers added
data = {
    "192020038": {
        "name": "Faiz Shaikh",
        "major": "DataScience",
        "starting_year": 2022,
        "total_attendance": 0,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34",
        "phone_number": "+919867720728"
    },
    "10": {
        "name": "OM Darekar",
        "major": "IOT",
        "starting_year": 2022,
        "total_attendance": 0,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34",
        "phone_number": "+918104825559"
    },
    "321654": {
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34",
        "phone_number": "+919867720728"
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34",
        "phone_number": "+919867720728"
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34",
        "phone_number": "+919221077408"
    }
}

# Add data to Firebase
for key, value in data.items():
    ref.child(key).set(value)

print("Data uploaded successfully!")
