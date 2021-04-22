import json
from uber import app

def test_index(app, client):
    del app
    res = client.get('/health')
    assert res.status_code == 200
    expected = "Hello from Python application"
    assert expected == json.loads(res.get_data(as_text=True))
