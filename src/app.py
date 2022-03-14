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
URL = f"https://gateway.marvel.com:443/v1/public/characters?ts={TS}&apikey={PUBLIC_KEY}&hash={HASHED}"

response = requests.get(URL)

if response.status_code==200:
  response_json = json.loads(response.text)
  pprint(response_json["data"]["results"][0])