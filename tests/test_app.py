import json


def test_index(app, client):
    res = client.get('/unittest')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))
