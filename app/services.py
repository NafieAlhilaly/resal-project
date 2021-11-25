async def is_csv(file_name: str) -> bool:
    """check if given file is a csv or not"""

    file_extention = file_name.split(".")[1]
    
    if file_extention == "csv":
        return True
    
    return False