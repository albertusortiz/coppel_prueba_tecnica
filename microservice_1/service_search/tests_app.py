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
url_searchComic_character = "http://localhost:3030/searchComics/Abyss"
response_character = requests.get(url_searchComic_character)
response_body_character = response_character.json()
response_searchComic_character = {
        "appearances": 8,
        "id": 1009149,
        "image": "http://i.annihil.us/u/prod/marvel/i/mg/9/30/535feab462a64.jpg",
        "name": "Abyss"
    }

# def test_get_character_for_abyss_check_content_type_equals_json():
#     assert response_body_character.headers["Content-Type"] == "application/json"

def test_get_details_for_character_abyss():
    assert response_searchComic_character == response_body_character

def test_get_id_for_abyss_check_equals_1009149():
    assert response_searchComic_character["id"] == int(response_body_character["id"])

def test_get_fields_from_character_and_check_four_fields_is_returned():
    assert len(response_body_character) == 4


""" Tests for search a Comic

In this cases we can test different escenaries."""

def test_get_url_comics_status_code_equals_200():
    response = requests.get(app.URL_COMICS)
    assert response.status_code == 200

def test_get_url_comics_status_code_equals_409():
    response = requests.get(app.URL_COMICS+"&comics")
    assert response.status_code == 409

# ULTIMATE X-MEN VOL. 5: ULTIMATE WAR TPB (Trade Paperback)
# is a comic from Marvel
comic = "ULTIMATE X-MEN VOL. 5: ULTIMATE WAR TPB (Trade Paperback)"
url_searchComic_comic = "http://localhost:3030/searchComics/" + comic
response_comic = requests.get(url_searchComic_comic)
response_body_comic = response_comic.json()
response_searchComic_comic = {
        "id": 1158,
        "image": "http://i.annihil.us/u/prod/marvel/i/mg/2/f0/4bc6670c80007.jpg",
        "onsaleDate": "2029-12-31T00:00:00-0500",
        "title": "ULTIMATE X-MEN VOL. 5: ULTIMATE WAR TPB (Trade Paperback)"
    }

# def test_get_comic_for_abyss_check_content_type_equals_json():
#     assert response_body_comic.headers["Content-Type"] == "application/json"

def test_get_details_for_comic_xmen():
    assert response_searchComic_comic == response_body_comic

def test_get_id_for_xmen_check_equals_1158():
    assert response_searchComic_comic["id"] == int(response_body_comic["id"])

def test_get_fields_from_comic_and_check_four_fields_is_returned():
    assert len(response_body_comic) == 4