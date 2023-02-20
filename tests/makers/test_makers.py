from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_makers_list():
    response = client.get("/hs/makers/list")
    assert response.status_code == 200
    assert response.json() == [{
        "markingDeletion": False,
        "id": 1,
        "name": "new_name"
    }]


def test_makers_change():
    response = client.put("/hs/makers/change/1",
                          json={"name": "new_name"}
                          )
    assert response.status_code == 200
    assert response.json() == "Maker changed successfully!"
