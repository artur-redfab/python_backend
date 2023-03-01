from fastapi.testclient import TestClient
from configparser import ConfigParser
from main import app

configP = ConfigParser()
configP.read('messages.ini')

client = TestClient(app)


#def test_tasks_delete():
#    response = client.delete("/hs/task/delete/1")
#    assert response.status_code == 404
#    assert response.text == "Task marked for deletion!"


def test_tasks_get_features():
    res = client.get('/hs/task/features/6')
    assert res.status_code == 200
    assert res.json() == {
            "id": "6",
            "name": "name",
            "idProject": "1",
            "idPriority": "1",
            "numberCopies": 1,
            "planPrintTime": 10800,
            "twoExtrPrint": True,
            "idBasicMaterial": "1",
            "idSupportMaterial": "1",
            "idBasicColor": "1",
            "idSupportColor": "1",
            "idOperGroup": "1",
            "volume": 3,
            "project": "newnamg",
            "factPrintTime": None,
            "basicMaterial": "string",
            "basicColor": "red",
            "supportMaterial": "string",
            "supportColor": "red",
            "idNozzleType": None,
            "nozzleType": None,
            "idNozzleSize": None,
            "nozzleSize": None,
            "operGroup": None,
            "idFile": None,
            "nameFile": None,
            "extFile": None,
            "sizeFile": None,
            "hashFile": None,
            "markingDeletion": True
            }


#def test_tasks_create():
#    response = client.post("/hs/task/create",
#                           json={
#                                "name": "fortest",
#                                "idProject": "1",
#                                "idPriority": "1",
#                                "numberCopies": 1,
#                                "planPrintTime": "03:00:00",
#                                "twoExtrPrint": True,
#                                "idBasicMaterial": "1",
#                                "idSupportMaterial": "1",
#                                "idBasicColor": "1",
#                                "idSupportColor": "1",
#                                "idOperGroup": "1",
#                                "volume": 3
#                           })
#    assert response.status_code == 200
#    assert response.json() == [{
#        "id": 1
#    }]



#def test_makers_change():
#    response = client.put("/hs/makers/change/1",
#                          json={"name": "new_name"}
#                          )
#    assert response.status_code == 200
#    assert response.json() == "Maker changed successfully!"