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
    
    # look for 'customer_average_rating' and 'product_name' in the columns
    if "product_name" not in list(df.columns):
        return {"msg": "err : could not find 'product_name' column"}
    elif "customer_average_rating" not in list(df.columns):
        return {"msg": "err : could not find 'customer_average_rating' column"}
    
    top_products = df[df['customer_average_rating'] >= df['customer_average_rating'].max()]
    
    return {"top_products": top_products.to_dict()}