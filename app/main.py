from fastapi import FastAPI, File, UploadFile, BackgroundTasks, HTTPException
from app import services

app = FastAPI()

@app.post("/upload")
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if file.filename.split(".")[1] != "csv":
        raise HTTPException(status_code=415, detail="Unsupported media type")
    background_tasks.add_task(services.handle_uploaded_file, file.file.read(), file.filename, True)
    return {"message": "file received, processing your file, you'll be notified when we finish proccessing"}