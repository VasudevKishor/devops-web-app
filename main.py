
# Importing the necessary modules from the Flask library
# Flask is used to create the web application, and jsonify is used to format the response as JSON
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, DevOps!")

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# This is a simple Flask application that returns a JSON response with a greeting message.