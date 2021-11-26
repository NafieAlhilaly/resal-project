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
            False) == '{"top_products": ["Massoub gift card"], "product_rating": [5.0]}'


def test_handle_uploaded_file_with_duplicates():
    """
    test uploaded file without duplicated data(same rating)
    """

    with open("tests/sample data files/sample_data_duplicates.csv") as file:
        assert services.handle_uploaded_file(
            file, 
            os.path.basename(file.name), 
            False) == '{"top_products": ["Arekah gift card", "Massoub gift card"], "product_rating": [5.0, 5.0]}'


def test_handle_uploaded_file_no_average_column():
    """
    test uploaded file with missing column 'customer_average_rating'
    """

    with open("tests/sample data files/sample_data_without_average_column.csv") as file:
        assert services.handle_uploaded_file(
            file, 
            os.path.basename(file.name), 
            False) == {'msg': "err : could not find 'customer_average_rating' column"}

def test_handle_uploaded_file_no_product_column():
    """
    test uploaded file with missing column 'product_name'
    """

    with open("tests/sample data files/sample_data_without_product_column.csv") as file:
        assert services.handle_uploaded_file(
            file, 
            os.path.basename(file.name), 
            False) == {'msg': "err : could not find 'product_name' column"}
