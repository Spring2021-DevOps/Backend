import json


def test_index(app, client):
    res = client.get('/health')
    assert res.status_code == 200
    expected = "Hello from Python application"
    assert expected == res.get_data(as_text=True)   