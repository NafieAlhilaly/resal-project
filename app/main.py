from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from app import services

app = FastAPI()

@app.post("/upload")
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    background_tasks.add_task(services.handle_file, file.file.read(), file.filename, True)
    return {"message": "file received, processing your file, you'll be notified when we finish proccessing"}