from io import BytesIO
from typing import Any, Callable, Union
import pandas as pd

def is_csv(file_name: str) -> bool:
    """
    check if given file is a csv or not
    
    param: 
        file_name: name of the file as string like 'file.extension'

    return: True if file_name contains csv, False if not
    """

    file_extention = file_name.split(".")[1]
    
    if file_extention == "csv":
        return True
    
    return False

def send_notifications(content: Any = None, msg: str = "Your file is ready") -> dict:
    """
    send notifiction to user when file is done proccessing

    params:
        content: any type , extended content for the message default value is None
        msg: str type , a notification main message default value is 'Your file is ready'

    return: dict of the message and content
    """
    return {"msg": msg, "content": content}

def handle_file(file: Any, from_memory: bool = True) -> Callable:
    """ 
    Handle uploaded file, check if it .csv and then extract top rating
    products information from it.

    params:
        from_memory: is true if file is a temporary file in memory 
        else it will read file from local storage

        file: if from_memory is True file is expected to be a string representation of the file, if False
            file is string path in local storage

    return :
        it will return dict if no errors
        or return a dict with error message if any error happens
    """

    if from_memory:
        df = pd.read_csv(BytesIO(file))
    else:
        df = pd.read_csv(file)

    # look for 'customer_average_rating' and 'product_name' in the columns
    if "product_name" not in list(df.columns):
        return send_notifications(msg="err : could not find 'product_name' column")
    elif "customer_average_rating" not in list(df.columns):
        return send_notifications(msg="err : could not find 'customer_average_rating' column")
    
    top_products = df[df['customer_average_rating'] >= df['customer_average_rating'].max()]
    
    top_products = {"top_products":list(top_products['product_name']), "products_rating":list(top_products['customer_average_rating'])[0]}
    
    return send_notifications(content=top_products)
