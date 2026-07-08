from fastapi.testclient import TestClient

def test_list_meals_returns_stubbed_meals(client: TestClient) -> None:
    response = client.get("/api/v1/meals")

    assert response.status_code == 200

    payload = response.json()
    assert len(payload) == 2
    assert payload[0]["name"] == "Breakfast bowl"
    assert payload[0]["protein_grams"] == 30
    assert payload[1]["name"] == "Chicken lunch"
    assert payload[1]["carb_grams"] == 58
