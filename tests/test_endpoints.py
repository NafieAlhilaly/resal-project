from app import main
import os
from fastapi.testclient import TestClient

client = TestClient(main.app)

def test_upload_csv():
    """Test upload endpoint if file is recieved and it is a csv file"""
    file = open("tests/sample data files/sample_data.csv")
    
    response = client.post("/upload", files={"file": (os.path.basename(file.name), file, "text/csv")})

    response.status_code == 202
    response.json() == {"message": "file received, processing your file, you'll be notified when we finish proccessing"}

def test_upload_not_csv():
    """Test upload endpoint if file is recieved and not a csv file"""
    file = open("tests/__init__.py")
    
    response = client.post("/upload", files={"file": (os.path.basename(file.name), file, "text/csv")})

    response.status_code == 202
    response.json() == {"detail": "Not a csv file"}