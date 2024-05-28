from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    #print("response", response.json())
    assert response.json() == {
  "id": "foo",
  "tittle": "Fooo",
  "description": "this is foo"
}

'''def test_read_item_bad_token():
    response=client.get("/items/foo",headers={"x-Token":"hailhydra"})
    assert response.status_code ==404
    print("response", response.json())
    assert response.json()'''


