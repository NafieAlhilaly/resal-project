from app import services

def test_is_csv():
    """ 
    test if the given file extension is 'csv' or not
    """

    file: str = "awesome_file_name.csv"
    assert services.is_csv(file) == True