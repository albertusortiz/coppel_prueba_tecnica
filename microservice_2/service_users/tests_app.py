import requests

endpoint_get_users = "http://localhost:6060/users"
response = requests.get(endpoint_get_users)
response_body = response.json()
response_user_0 = {
        "_id": {
            "$oid": "622f976eda77b4c3c6a9c2f5"
        },
        "name": "Alberto Ortiz",
        "age": "30",
        "username": "albertusortiz",
        "email": "albertusortiz@gmail.com",
        "password": "pbkdf2:sha256:260000$n3HQWmfTt52pt2BQ$3dca7c1daee43f4dcceeeb2aae9cbfed2eb649426b5f0ccce7aa80771693711a",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NzI4NjEyNiwianRpIjoiZjY2M2FhZjUtODg0MC00OGQ3LWI3OWUtMzA5YmU1NzEwN2QxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkFsYmVydG8gT3J0aXoiLCJuYmYiOjE2NDcyODYxMjYsImV4cCI6MTY0NzM3MjUyNn0.uYZqAKgzwmMw_JtgyzF8XDpWkLOv2A-efAd6Y-SJcAk"
    }

def test_get_url_users_status_code_equals_200():
    response = requests.get(endpoint_get_users)
    assert response.status_code == 200

def test_get_url_users_status_code_equals_404():
    response = requests.get(endpoint_get_users[:-1])
    assert response.status_code == 404

def test_get_character_for_abyss_check_content_type_equals_json():
    assert response.headers["Content-Type"] == "application/json"

def test_get_details_for_user():
    assert response_user_0 == response_body[0]

def test_get_name_for_user_equals_alberto_ortiz():
    assert response_user_0["name"] == response_body[0]["name"]

def test_get_fields_from_user_and_check_seven_fields_is_returned():
    assert len(response_body[0]) == 7