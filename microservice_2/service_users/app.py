import os
import json
import requests

from dotenv import load_dotenv
from pprint import pprint
from flask import Flask, jsonify, request, Response

load_dotenv()

app = Flask(__name__)


@app.route('/hello', methods=["GET"])
def hello(search):
    return jsonify({"message": "Hola mundo"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2000, debug=True)
