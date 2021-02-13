import json

def test_licence_post_with_incorrect_key(app, client):
    data = {
                "first_name": "Jordan",
                "surname": "Ball",
                "date_of_birth":"1996-02-17",
                "gender":"M"
            }

    response = client.post(
        "/licence",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400

def test_licence_post_without_key(app, client):
    data = {
                "first_name": "Jordan",
                "last_name": "Ball",
                "date_of_birth":"1996-02-17"
            }

    response = client.post(
        "/licence",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400

def test_licence_post(app, client):
    data = {
                "first_name": "Jordan",
                "last_name": "Ball",
                "date_of_birth":"1996-02-17",
                "gender":"M"
            }

    response = client.post(
        "/licence",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 200

def test_licence_post_with_bad_data_format(app, client):
    data = {
                "first_name": "Jordan",
                "last_name": "Ball",
                "date_of_birth":"96-02-17",
                "gender":"M"
            }

    response = client.post(
        "/licence",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400

def test_licence_post_with_incorrect_gender(app, client):
    data = {
                "first_name": "Jordan",
                "last_name": "Ball",
                "date_of_birth":"1996-02-17",
                "gender":"Male"
            }

    response = client.post(
        "/licence",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400
