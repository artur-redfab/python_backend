from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_tasks_create():
    response = client.post("/hs/task/create",
                           json={
                                "name": "fortest",
                                "idProject": "1",
                                "idPriority": "1",
                                "numberCopies": 1,
                                "planPrintTime": "03:00:00",
                                "twoExtrPrint": True,
                                "idBasicMaterial": "1",
                                "idSupportMaterial": "1",
                                "idBasicColor": "1",
                                "idSupportColor": "1",
                                "idOperGroup": "1",
                                "volume": 3
                           })
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1
    }]



#def test_makers_change():
#    response = client.put("/hs/makers/change/1",
#                          json={"name": "new_name"}
#                          )
#    assert response.status_code == 200
#    assert response.json() == "Maker changed successfully!"