import os
import random
from app import services

def test_is_csv() -> None:
    """ 
    test if the given file is csv
    """

    file: str = "awesome_file_name.csv"
    assert services.is_csv(file) == True

def test_is_not_csv() -> None:
    """ 
    test if the given file is not csv
    """

    file: str = "file_name.pdf"
    assert services.is_csv(file) == False

def test_handle_file_no_duplicates() -> None:
    """
    test uploaded file without duplicated data(same rating)
    """

    with open("tests/sample data files/sample_data.csv") as file:
        assert services.handle_file(
            file,
            False) == {'msg': 'Your file is ready', 'content': {'top_products': ['Massoub gift card'], 'products_rating': 5.0}}


def test_handle_file_duplicates() -> None:
    """
    test uploaded file without duplicated data(same rating)
    """

    with open("tests/sample data files/sample_data_duplicates.csv") as file:
        assert services.handle_file(
            file,
            False) == {'msg': 'Your file is ready', 'content': {'top_products': ['Arekah gift card', 'Massoub gift card'], 'products_rating': 5.0}}


def test_handle_file_no_average_column() -> None:
    """
    test uploaded file with missing column 'customer_average_rating' or typos in it
    """

    with open("tests/sample data files/sample_data_without_average_column.csv") as file:
        assert services.handle_file(
            file,
            False) == {'msg': "err : could not find 'customer_average_rating' column", 'content': None}

def test_handle_file_no_product_column() -> None:
    """
    test uploaded file with missing column 'product_name' or typos in it
    """

    with open("tests/sample data files/sample_data_without_product_column.csv") as file:
        assert services.handle_file(
            file,
            False) == {'msg': "err : could not find 'product_name' column", 'content': None}

def test_send_notifications_default() -> None:
    """
    test send notifications with defaults
    """

    assert services.send_notifications() == {"msg": "Your file is ready", "content": None}

def test_send_notifications_random_params() -> None:
    """
    test send notifications with given random messages and content
    """

    msgs = [
        "File is ready",
        "Your file is done",
        "File done prccessing",
        "File ready!",
        "Your data is ready",
        "Data done proccessing",
        "Data ready"
    ]
    files = [
        "top_products.csv",
        "top_products.json",
        "top_products.xlsx"
    ]
    msg = random.choice(msgs)
    file = random.choice(files)

    assert services.send_notifications(msg=msg, content=file) == {"msg":msg, "content":file}


def test_handle_large_data():
    """
    Test large_data.csv(2M rows) 
    """

    with open("tests/sample data files/large_data.csv") as file:
        assert type(services.handle_file(file, False)) is dict