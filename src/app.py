import os
import json
import requests

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TS=1
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
HASHED = os.getenv('HASHED')
URL_CHARACTERS = f"https://gateway.marvel.com:443/v1/public/characters?ts={TS}&apikey={PUBLIC_KEY}&hash={HASHED}"

response_characters = requests.get(URL_CHARACTERS)

if response_characters.status_code==200:
  response_json = json.loads(response_characters.text)

  for character in response_json["data"]["results"]:
    
    character_to_search = "3-D Man"
    
    if character["name"] in character_to_search:
      id = character["id"]
      name = character["name"]
      image = character["thumbnail"]["path"]+"."+character["thumbnail"]["extension"]
      appearances = character["comics"]["available"]

      dic = {
        "id":id,
        "name":name,
        "image":image,
        "appearances":appearances
      }

      pprint(dic)