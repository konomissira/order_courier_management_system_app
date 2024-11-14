from unittest.mock import patch
from database_management.manage_products_database import create_new_product, products_list

def test_create_new_product():
    # Check initial length of products_list
    initial_length = len(products_list)
    
    # Define product details
    product_name = "Test Product"
    product_price = 10.99

    # Run the function with patched input
    with patch("builtins.input", side_effect=[product_name, str(product_price)]):
        create_new_product()

    # Verify the length increased by one
    assert len(products_list) == initial_length + 1

    # Check that the last item in products_list is the new product
    assert products_list[-1] == {
        'product_name': product_name,
        'product_price': product_price
    }