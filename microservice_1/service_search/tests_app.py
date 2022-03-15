import requests
import app

""" Tests for search a Character

In this cases we can test different escenaries."""

def test_get_url_characters_status_code_equals_200():
    response = requests.get(app.URL_CHARACTERS)
    assert response.status_code == 200

def test_get_url_characters_status_code_equals_409():
    response = requests.get(app.URL_CHARACTERS+"&character")
    assert response.status_code == 409

# Abyss is a character from Marvel
url_searchComic = "http://localhost:3030/searchComics/Abyss"
response = requests.get(url_searchComic)
response_body = response.json()
response_searchComic = {
        "appearances": 8,
        "id": 1009149,
        "image": "http://i.annihil.us/u/prod/marvel/i/mg/9/30/535feab462a64.jpg",
        "name": "Abyss"
    }

def test_get_character_for_abyss_check_content_type_equals_json():
    assert response.headers["Content-Type"] == "application/json"

def test_get_details_for_character_abyss():
    assert response_searchComic == response_body

def test_get_id_for_abyss_check_equals_1009149():
    assert response_searchComic["id"] == int(response_body["id"])

def test_get_fields_from_character_and_check_four_fields_is_returned():
    assert len(response_body) == 4


# Tests for search a Comic

def test_get_url_comics_status_code_equals_200():
    response = requests.get(app.URL_COMICS)
    assert response.status_code == 200

def test_get_url_comics_status_code_equals_409():
    response = requests.get(app.URL_COMICS+"&comics")
    assert response.status_code == 409