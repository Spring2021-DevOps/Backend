import pytest

from uber import app


@pytest.fixture
def app():
    yield app


@pytest.fixture
def client(app):
    return app.test_client()