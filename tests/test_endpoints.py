from app import main
from fastapi.testclient import TestClient

client = TestClient(main.app)

def test_upload():
    """Test upload endpoint if status_code is 200(ok)"""

    response = client.post("/upload")
    response.status_code == 200
    response.json() == {"message": "file received, processing your file..."}
