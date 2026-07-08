import pytest
from fastapi.testclient import TestClient

from pfc_calc.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
