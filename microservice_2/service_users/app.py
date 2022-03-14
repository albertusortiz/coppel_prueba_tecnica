import os
import datetime

from dotenv import load_dotenv
from pprint import pprint

from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo, MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


load_dotenv()

NAME_DATABASE = os.getenv("NAME_DATABASE")
USER_DATABASE = os.getenv("USER_DATABASE")
PASSWORD_DATABASE = os.getenv("PASSWORD_DATABASE")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.config["MONGO_URI"] = f"mongodb+srv://{USER_DATABASE}:{PASSWORD_DATABASE}@cluster0.ajhif.mongodb.net/{NAME_DATABASE}?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route('/hello', methods=["GET"])
def hello():
    return jsonify({"message": "Hola mundo"})


@app.route('/users', methods=['POST'])
def create_user():
    # Receiving data
    name = request.json["name"]
    age = request.json["age"]
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]

    if username and email and password:
        hashed_password = generate_password_hash(password)
        access_token = create_access_token(identity=name)
        id = mongo.db.users.insert_one(
            {
                'name': name,
                'age': age,
                'username': username,
                'email': email,
                'password': hashed_password,
                'token': access_token
            }
        )
        response = {
            'id': str(id),
            'name': name,
            'age': age,
            'username': username,
            'password': hashed_password,
            'email': email,
            'token': access_token
        }
        return response
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource not found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2000, debug=True)
