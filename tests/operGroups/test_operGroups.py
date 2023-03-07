from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_oper_group_get_list():
    res = client.get('/hs/operGroups/list')
    assert res.status_code == 200
    assert res.json() == [
        {
            "id": "3",
            "name": "opergroup 1",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "5",
            "name": "opeup 1",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "6",
            "name": "oeup 1",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "8",
            "name": "op 1",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "9",
            "name": "o 1",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "10",
            "name": "o",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "11",
            "name": "osss",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        },
        {
            "id": "1",
            "name": "testChange",
            "cluster": "testCluster",
            "nozzleType": "nozzletype666",
            "nozzleSize": "15559",
            "idCluster": "1",
            "idNozzleType": "1",
            "idNozzleSize": "1",
            "markingDeletion": False
        }
    ]


def test_oper_group_get_feature():
    res = client.get('/hs/operGroups/features/3')
    assert res.status_code == 200
    assert res.json() == {
        "id": 3,
        "name": "opergroup 1",
        "idCluster": 1,
        "idNozzleType": 1,
        "idNozzleSize": 1,
        "markingDeletion": False
    }


def test_oper_group_get_printer_list():
    res = client.get('/hs/operGroups/printerList/1')
    assert res.status_code == 200
    assert res.json() == [
        {
            "id": 1,
            "name": "testPrinter"
        }
    ]

