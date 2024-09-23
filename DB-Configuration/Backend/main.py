from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

# Flask is a web framework for Python that allows you to build web applications and APIs.
# __name__ special variable in Python that holds the name of the current module (script).
app = Flask(__name__)  # Create the Flask app instance

# Enable CORS for all routes
CORS(app)

# MySQL connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CK13",
    database="python_db_configure"
)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json

    # Extract data from request
    name = data['name']
    address = data['address']
    email = data['email']
    password = data['password']

    try:
        cursor = db.cursor()

        # Insert data into the database
        cursor.execute(
            "INSERT INTO users (name, address, email, password) VALUES (%s, %s, %s, %s)",
            (name, address, email, password)
        )
        db.commit()

        # jsonify is a Flask helper function that converts Python dictionaries into JSON (JavaScript Object Notation) format.
        # 200 is the HTTP status code.
        return jsonify({"message": "User registered successfully!"}), 200
    except Exception as e:
        # The f in front of the string allows for string interpolation (inserting the value of e into the string).
        print(f"Error: {e}")
        return jsonify({"message": "Registration failed!"}), 500


if __name__ == '__main__':
    app.run(debug=True)
