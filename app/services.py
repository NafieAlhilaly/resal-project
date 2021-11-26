from io import StringIO
from typing import Any, Optional, Union
import pandas as pd
import json

def is_csv(file_name: str) -> bool:
    """check if given file is a csv or not"""

    file_extention = file_name.split(".")[1]
    
    if file_extention == "csv":
        return True
    
    return False

def send_notifications(content: Any = None, msg: str = "Your file is ready") -> dict:
    """
    send notifiction to user when file is done proccessing
    """

    return {"msg": msg, "content": content}

def handle_uploaded_file(file: str , filename: str, from_memory: bool = True) -> Union[str, dict]:
    """ 
    Handle uploaded file, check if it .csv and then extract top rating
    products information from it.

    from_memory is true if file is a temporary file in memory 
    else it will read file as it is in local storage
    """

    if not is_csv(filename):
        return {"msg": "err : not a csv file"}

    if from_memory:
        df = pd.read_csv(StringIO(str(file, 'utf-8')), encoding='utf-8')
    else:
        df = pd.read_csv(file)

    # look for 'customer_average_rating' and 'product_name' in the columns
    if "product_name" not in list(df.columns):
        return {"msg": "err : could not find 'product_name' column"}
    elif "customer_average_rating" not in list(df.columns):
        return {"msg": "err : could not find 'customer_average_rating' column"}
    
    top_products = df[df['customer_average_rating'] >= df['customer_average_rating'].max()]
    
    top_products = {"top_products":list(top_products['product_name']), "product_rating":list(top_products['customer_average_rating'])}
    
    return json.dumps(top_products)
