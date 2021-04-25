import json


def test_index(app, client):
    res = client.get('/doc')
    assert res.status_code == 200
    expected = """Welcome to online mongo/uber testing ground!<br />
        <br />
        Run the following endpoints:<br />
        From collection:<br/>
        http://localhost:5000/bookings<br />
        http://localhost:5000/bookings-week<br />
        http://localhost:5000/bookings-week-results<br />
        Create new data:<br />
        http://localhost:5000/mock-bookings<br />
        Optionally, to purge database: http://localhost:5000/purge-db"""
    assert expected == res.get_data(as_text=True)   