from app import main
import os
from fastapi.testclient import TestClient

client = TestClient(main.app)

def test_upload_csv():
    """Test upload endpoint if file is recieved abd it is a csv file"""
    file = open("tests/sample data files/sample_data.csv")
    
    response = client.post("/upload", files={"file": (os.path.basename(file.name), file, "text/csv")})

    response.status_code == 202
    response.json() == {"message": "file received, processing your file, you'll be notified when we finish proccessing"}

