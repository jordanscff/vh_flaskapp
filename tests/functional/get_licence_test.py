def test_licence_get(app, client):
    res = client.get('/licence')
    assert res.status_code == 200
    licence_list = res.get_json()
    for item in licence_list:
        assert len(item) == 17
