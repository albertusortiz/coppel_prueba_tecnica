import os
import json
import requests

from dotenv import load_dotenv
from pprint import pprint
from flask import Flask, jsonify, request, Response

load_dotenv()

app = Flask(__name__)

TS=1
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
HASHED = os.getenv('HASHED')
URL_CHARACTERS = f"https://gateway.marvel.com:443/v1/public/characters?ts={TS}&apikey={PUBLIC_KEY}&hash={HASHED}"

@app.route('/searchComics/<search>', methods=["GET"])
def get_character(search):
  response_characters = requests.get(URL_CHARACTERS)

  if response_characters.status_code==200:
    response_json = json.loads(response_characters.text)

    for character in response_json["data"]["results"]:
      
      if character["name"] == search:
        id = character["id"]
        name = character["name"]
        image = character["thumbnail"]["path"]+"."+character["thumbnail"]["extension"]
        appearances = character["comics"]["available"]

        response = {
          "id":id,
          "name":name,
          "image":image,
          "appearances":appearances
        }
        return jsonify(response)
    response = jsonify({'message': 'No results for ' + search})
    return response

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=4000, debug=True)