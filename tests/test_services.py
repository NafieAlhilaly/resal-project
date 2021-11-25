from app import services

def test_is_csv():
    """ 
    test if the given file is csv
    """

    file: str = "awesome_file_name.csv"
    assert services.is_csv(file) == True

def test_is_not_csv():
    """ 
    test if the given file is not csv
    """

    file: str = "file_name.pdf"
    assert services.is_csv(file) == False