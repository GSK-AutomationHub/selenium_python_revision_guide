import pytest


def test_xyz():
    print("mandatory to run before valid product search test")

@pytest.mark.order(after="test_search_multiple_products_ddt")
def test_search_valid_product():
    print("verify search feature with valid product")

@pytest.mark.xfail
def test_search_invalid_product():
    print("verify search feature with invalid product")
    assert False

data_provider = ["HP Laptop","Rolex Watch","Reyban Specs"]
@pytest.mark.parametrize("product",data_provider)
@pytest.mark.ddt
@pytest.mark.order(after="test_xyz")
def test_search_multiple_products_ddt(product):
    print("verify search feature with multiple set of products")
    print(f"Searched product {product}")