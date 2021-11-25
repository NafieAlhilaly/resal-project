from fastapi import File, UploadFile
from io import StringIO
import pandas as pd

def is_csv(file_name: str) -> bool:
    """check if given file is a csv or not"""

    file_extention = file_name.split(".")[1]
    
    if file_extention == "csv":
        return True
    
    return False

def handle_uploaded_file(file: UploadFile = File(...)):
    """ 
    Handle uploaded file, check if it .csv and then extract top rating
    products information from it.
    """

    if not is_csv(file.filename):
        return {"msg": "err : not a csv file"}
    
    df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
    
    # look for 'customer_average_rating' and 'product_name' in the columns
    if "product_name" not in list(df.columns):
        return {"msg": "err : could not find 'product_name' column"}
    elif "customer_average_rating" not in list(df.columns):
        return {"msg": "err : could not find 'customer_average_rating' column"}
    
    top_products = df[df['customer_average_rating'] >= df['customer_average_rating'].max()]
    
    return {"top_products": top_products.to_dict()}
