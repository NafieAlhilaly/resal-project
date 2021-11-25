from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from io import StringIO
import pandas as pd
app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    
    df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
    
    return {"msg": file.filename}