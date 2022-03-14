import requests
import app


def test_get_url_characters_status_code_equals_200():
    response = requests.get(app.URL_CHARACTERS)
    assert response.status_code == 200
