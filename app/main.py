from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from io import StringIO
import pandas as pd
from app import services

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not await services.is_csv(file.filename):
        return {"msg": "err : not a csv file"}
    
    df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
    
    # look for 'customer_average_rating' in the columns
    if "customer_average_rating" not in df.columns and "product_name" not in df.columns :
        return {"msg": "err : could not find 'customer_average_rating' or 'product_name' column"}
    return {"msg": file.filename}