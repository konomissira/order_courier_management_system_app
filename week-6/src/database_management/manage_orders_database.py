from create_connection import cursor, conn

from manage_products_database import display_product_list, products_list
from manage_couriers_database import display_courier_list, couriers

# Load Data  From orders table in Database
def load_orders_from_db():
    try:
        cursor.execute("SELECT customer_name, customer_address, customer_phone, courier, status, items FROM orders")
        orders = cursor.fetchall()
        return [{'customer_name': row[0], 'customer_address': row[1], 'customer_phone': row[2],
                'courier': row[3], 'status': row[4], 'items': row[5]} for row in orders]
    except ValueError as e:
        print(f"An error occured while loading orders: {e}")
        return[]

def save_orders_to_db():
    try:
        # Clear Table before saving Data Into the Database
        cursor.execute("DELETE FROM orders")
        for order in orders:
            cursor.execute(
                "INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (order['customer_name'], order['customer_address'], order['customer_phone'],
                order['courier'], order['status'], order['items'])
            )
        conn.commit()
        print("Orders saved to database successfully.")
    except Exception as e:
        print(f"An error occured while saving orders: {e}")

orders = load_orders_from_db()

# Display Customer Order
def display_customer_order():
    print("Customer Orders:")
    for i, order in enumerate(orders):
        print(f"Order{i + 1} : Name: {order['customer_name']} - Phone: {order['customer_phone']}  - Status: {order['status']}")
    print('-' *70)

# Create New Order
def create_new_order():
    # Get customer details with validation
    while True:
        customer_name = input("Enter the customer's name: ").strip()
        if customer_name:
            break
        print("Customer name cannot be empty.")

    customer_address = input("Enter the customer's address: ").strip()

    while True:
        customer_phone = input("Enter the customer's phone number: ").strip()
        if customer_phone.isdigit() and 7 <= len(customer_phone) <= 15:
            break
        print("Please enter a valid phone number with 7-15 digits.")

    # Display product list and get a comma-separated list of product indexes
    display_product_list()
    while True:
        items = input("Enter the product numbers as a comma-separated list (e.g., 1,3,4): ").replace(" ", "")
        try:
            # Ensure all items are valid integers and within product list range
            product_indexes = [int(i) - 1 for i in items.split(",") if i]
            if all(0 <= idx < len(products_list) for idx in product_indexes):
                break
            else:
                print("One or more product numbers are invalid. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

    # Display couriers list and get courier selection with validation
    display_courier_list()
    while True:
        try:
            courier_index = int(input("Enter the courier number: ")) - 1
            if 0 <= courier_index < len(couriers):
                break
            else:
                print("Please enter a valid courier number.")
        except ValueError:
            print("Please enter a number.")

    # Set the initial status and create the new order dictionary
    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "courier": courier_index,
        "status": "preparing",
        "items": items  # Store the comma-separated string
    }

    # Append the new order to the orders list
    orders.append(new_order)
    print("New order created successfully!")

# Update Order Status
def update_existing_order_status():
    # Status options
    order_status_list = ["preparing", "out for delivery", "delivered"]

    # Display orders with index values
    print("Orders List:")
    for i, order in enumerate(orders):
        print(f"Order {i + 1}: Name: {order['customer_name']} - Status: {order['status']}")
    print("-" * 40)

    try:
        # Get the order index from the user
        order_index = int(input("Enter the order number to update: ")) - 1
        if 0 <= order_index < len(orders):
            selected_order = orders[order_index]

            # Display status options with index values
            print("\nOrder Status Options:")
            for i, status in enumerate(order_status_list):
                print(f"{i + 1}. {status}")
            print("-" * 40)

            # Get the new status index from the user
            status_index = int(input("Enter the new status number: ")) - 1
            if 0 <= status_index < len(order_status_list):
                # Update the order status
                selected_order["status"] = order_status_list[status_index]
                print("Order status updated successfully!")
            else:
                print("Invalid status number.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid number.")

# Update Existing Order
def update_existing_order():
    # Display orders list with index values
    print("Orders List:")
    for i, order in enumerate(orders):
        print(f"Order {i + 1}: Name: {order['customer_name']} - Address: {order['customer_address']} - Phone: {order['customer_phone']} - Courier: {order['courier']} - Status: {order['status']} - Items: {order['items']}")
    print("-" * 40)

    try:
        # Get the order index from the user
        order_index = int(input("Enter the order number to update: ")) - 1
        if 0 <= order_index < len(orders):
            selected_order = orders[order_index]

            # Iterate over each key-value pair in the selected order
            for key, value in selected_order.items():
                # Prompt the user for a new value, showing the current value
                new_value = input(f"Enter new {key} (leave blank to keep '{value}'): ").strip()
                
                # Update the property only if new input is provided
                if new_value:
                    if key == "courier":
                        if new_value.isdigit() and 0 <= int(new_value) - 1 < len(couriers):
                            selected_order[key] = int(new_value) - 1
                        else:
                            print("Invalid courier number.")
                    elif key == "items":
                        selected_order[key] = new_value.replace(" ", "")  # Clean up items string
                    else:
                        selected_order[key] = new_value

            print("Order updated successfully!")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete order
def delete_order():
    if not orders:
        print("No orders to delete.")
        return
    
    # Display orders list with index values
    print("Orders List:")
    for i, order in enumerate(orders):
        print(f"Order {i + 1}: Name: {order['customer_name']} - Phone: {order['customer_phone']} - Status: {order['status']}")
    print("-" * 40)

    try:
        # Get the order index from the user
        order_index = int(input("Enter the order number to delete: ")) - 1
        
        # Check if the index is valid
        if 0 <= order_index < len(orders):
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete Order {order_index + 1}? (yes/no): ").strip().lower()
            if confirm == "yes":
                # Delete the order
                orders.pop(order_index)
                print("Order deleted successfully!")
            else:
                print("Order deletion canceled.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid number.")
