from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from io import StringIO
import pandas as pd
from app import services

app = FastAPI()

@app.post("/upload")
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    background_tasks.add_task(services.handle_uploaded_file, file)
    return {"message": "file received, processing your file..."}