from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_projects_get_features():
    res = client.get('/hs/project/features/1')
    assert res.status_code == 200
    assert res.json() == {
                "id": "1",
                "name": "newnamg",
                "idPriority": "1",
                "createDate": "2023-02-17T11:01:45.475042+03:00",
                "deadLine": "2023-02-16T00:00:00+03:00",
                "changeDate": None,
                "orderNumber": "string",
                "idPartner": "1",
                "idResponsible": "5",
                "author": "done",
                "idProjectStatus": None,
                "comment": "string",
                "markingDeletion": False
            }


