from unittest.mock import patch
from database_management.manage_couriers_database import create_new_courier, couriers

def test_create_new_courier():
    # Check the initial length of couriers
    initial_length = len(couriers)
    
    # Define courier details
    courier_name = "Test Courier"
    courier_phone = "1234567890"

    # Run the function with patched input
    with patch("builtins.input", side_effect=[courier_name, courier_phone]):
        create_new_courier()

    # Verify the length increased by one
    assert len(couriers) == initial_length + 1

    # Check that the last item in couriers is the new courier
    assert couriers[-1] == {
        'courier_name': courier_name,
        'courier_phone_number': courier_phone
    }