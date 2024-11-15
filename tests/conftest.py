import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# toda vez que client for chamado, será retornado na função
@pytest.fixture
def client():
    return TestClient(app)
