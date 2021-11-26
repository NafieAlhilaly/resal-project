import os
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

def test_handle_uploaded_file_no_duplicates():
    """
    test uploaded file without duplicated data(same rating)
    """

    with open("tests/sample data files/sample_data.csv") as file:
        assert services.handle_uploaded_file(
            file, 
            os.path.basename(file.name), 
            False) == {'top_products': {'customer_average_rating': {0: 5.0}, 'id': {0: 123}, 'product_name': {0: 'Massoub gift card'}}}

def test_handle_uploaded_file_with_duplicates():
    """
    test uploaded file without duplicated data(same rating)
    """

    with open("tests/sample data files/sample_data_duplicates.csv") as file:
        assert services.handle_uploaded_file(
            file, 
            os.path.basename(file.name), 
            False) == {'top_products': {'customer_average_rating': {0: 5.0, 1: 5.0}, 'id': {0: 126, 1: 123}, 'product_name': {0: 'Arekah gift card', 1: 'Massoub gift card'}}}

def test_handle_uploaded_file_no_average_column():
    """
    test uploaded file with missing column 'customer_average_rating'
    """

    with open("tests/sample data files/sample_data_without_average_column.csv") as file:
        assert services.handle_uploaded_file(
            file, 
            os.path.basename(file.name), 
            False) == {'msg': "err : could not find 'customer_average_rating' column"}