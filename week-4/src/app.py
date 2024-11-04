import json
import csv

# File Handling Functions
def read_file(file_name):
    """Reads a text file and returns the contents as a list of lines."""
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []  # Return an empty list if file not found

def write_file(file_name, data):
    """Writes a list of items to a text file, each item on a new line."""
    with open(file_name, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def read_json(file_name):
    """Reads a JSON file and returns the data."""
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file not found

def write_json(file_name, data):
    """Writes data to a JSON file."""
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def save_products_list_to_csv():
    with open('../csv_folder/products_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['product_name', 'product_price'])

        for product in products_list:
            writer.writerow([product['name'], product['price']])

def save_courier_to_csv():
    with open('../csv_folder/couriers.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['courier_name', 'courier_phone_number'])
        for courier in couriers:
            writer.writerow([courier['name'], courier['phone']])

def save_orders_to_csv():
    with open('../csv_folder/orders.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Create Header for CSV File.
        writer.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
        for order in orders:
            writer.writerow([order['customer_name'], order['customer_address'], order['customer_phone'], order['courier'], order['status'], order['items']])


# Main Menu
menu_options = ['Exit App', 'Print Products Menu', 'Print Couriers Menu', 'Print Orders Menu']

# Products Menu
products_menu = ['Return to Main Menu', 'Print Products List', 'Add new Product', 'Update Existing Product', 'Delete Product']

# Orders Menu
orders_menu = ['Return to Main Menu', 'Print Customer Order', 'Create New Order', 'Update Existing Order Status', 'Update Existing Order', 'Delete Order']

# Couriers Menu
couriers_menu = ['Return to Main Menu', 'Print Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']

# Load data from files
products_list = read_json('../data/products_list.json')
couriers = read_json('../data/couriers.json')
orders = read_json('../data/orders.json')

# Display Main Menu
def display_main_menu():
    print("Main Menu:")
    for i, option in enumerate(menu_options):
        print(f"{i} : {option}")
    print()

# Display Menu Product
def display_menu_product():
    print("Products Menu:")
    for i, option in enumerate(products_menu):
        print(f"{i} : {option}")
    print("-" *50)

# Display Menu Order
def display_menu_order():
    print("Orders Menu:")
    for i, option in enumerate(orders_menu):
        print(f"{i} : {option}")
    print("-" *50)

# Display Product List
def display_product_list():
    print("Products List:")
    print("-" * 50)
    for i, product in enumerate(products_list):
        print(f"Product - {i + 1} {product['name']} : £{product['price']:.2f}")
    print('-' * 50)

# Add New Product
def create_new_product():
    new_product_name = input('Enter the product name: ')
                    
    while True:
        try:
            new_product_price = float(input('Enter the product price: '))
            break
        except ValueError:
            print('Please enter a numeric value!')

    new_product = {
        'name':new_product_name,
        'price':new_product_price
    }
    # Append New Product to product_list
    products_list.append(new_product)
    print(f'New product: {new_product_name} added successfully')

# Update Existing Product
def update_existing_product():
        display_product_list()

        product_index = int(input('Enter the product number to update: ')) - 1
        if 0 <= product_index < len(products_list):
            product_to_update = products_list[product_index]

            for key, value in product_to_update.items():
                new_value = input(f"Enter new {key} (leave blank to keep '{value}'): ")
                if new_value.strip():
                    if key == 'price':
                        product_to_update[key] = float(new_value)
                    else:
                        product_to_update[key] = new_value
            print('Product updated successfully')
        else:
            print('Invalid product number')

# Delete Product
def delete_product():
    display_product_list()

    try:
        remove_product = int(input('Enter the product number to delete: ')) - 1
        if 0 <= remove_product < len(products_list):
            to_confirm = input(f"Are you sure you want to delete {products_list[remove_product]['name']} ? (yes/no):  ")
            if to_confirm.lower() == 'yes':
                products_list.pop(remove_product)
                print("Product deleted successfully.")
    except ValueError:
        print('Invalid input. Please, enter a numeric value.')

# Display Menu Courier
def display_menu_courier():
    print('Couriers Menu')
    for i, option in enumerate(couriers_menu):
        print(f'{i} : {option}')
    print()

# Display Courier List
def display_courier_list():
    print("Courier List:")
    print('-' *50)

    for i, courier in enumerate(couriers):
        print(f"Courier {i + 1} Name: {courier['name']} - Phone Number: {courier['phone']}")
    print('-' *50)

# Create New Courier
def create_new_courier():
    courier_name = input('Enter the courier name: ')
    courier_phone_number = input('Enter the courier number: ')

    new_courier = {
        'name': courier_name,
        'phone': courier_phone_number
    }

    couriers.append(new_courier)

# Update Existing Courier
def update_existing_courier():
    display_courier_list()

    courier_index = int(input('Enter the courier number to update: ')) - 1

    if 0 <= courier_index < len(couriers):
        selected_courier = couriers[courier_index]
        for key, value in selected_courier.items():
            new_courier_value = input(f"Enter new {key} (leave blank to keep '{value}'): ")
            if new_courier_value.strip():
                selected_courier[key] = new_courier_value
        print('Courier updated successfully.')
    else:
        print('Invalid courier number')

# Delete Courier
def delete_courier():
    display_courier_list()
    try:
        courier_index = int(input("Enter the courier number to delete: ")) - 1
        if 0 <= courier_index < len(couriers):
            confirm_delete_courier = input(f"Are you sure you want to delete {couriers[courier_index]['name']} ? (yes/no):  ")
            if confirm_delete_courier.lower() == 'yes':
                couriers.pop(courier_index)
                print(f"Courier deleted successfully.")
        else:
            print("Invalid courier number.")
    except ValueError:
        print("Please enter a valid number.")

# Display Customer Order
def display_customer_order():
    print("Customer Orders:")
    for i, order in enumerate(orders):
        print(f"Order{i + 1} : Name: {order['customer_name']} - Phone: {order['customer_phone']}  - Status: {order['status']}")
    print('-' *70)

# Create New Order
def create_new_order():
    # Get customer details
    customer_name = input("Enter the customer's name: ")
    customer_address = input("Enter the customer's address: ")
    customer_phone = input("Enter the customer's phone number: ")

    # Display product list and get a comma-separated list of product indexes
    display_product_list()
    items = input("Enter the product numbers as a comma-separated list (e.g., 1,3,4): ")
    items = items.replace(" ", "")  # Remove any spaces for a clean input string

    # Display couriers list to get courier selection
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
                    # Convert to int if updating courier or items
                    if key in ["courier"]:
                        selected_order[key] = int(new_value)
                    elif key == "items":
                        selected_order[key] = new_value.replace(" ", "")  # Remove spaces for a clean items string
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



# Main app loop
def main():
    do_loop = True

    while do_loop:
        display_main_menu()
        user_input = int(input('Choose an Option: '))

        if user_input == 0:
            # Save data to files
            write_json('../data/couriers.json', couriers)
            write_json('../data/products_list.json', products_list)
            write_json('../data/orders.json', orders)
            save_products_list_to_csv()
            save_courier_to_csv()
            save_orders_to_csv()
            
            print("Exiting app... Data saved.")
            do_loop = False
        elif user_input == 1:
            product_loop = True
            while product_loop:
                display_menu_product()
                product_input = int(input('Choose an Option: '))
                print("-" *50)

                if product_input == 0:
                    product_loop = False
                elif product_input == 1:
                    display_product_list()
                elif product_input == 2:
                    create_new_product()
                elif product_input == 3:
                    update_existing_product()
                elif product_input == 4:
                    delete_product()
                else:
                    print("Invalid option. Please try again.")
        elif user_input == 2:
            courier_loop = True
            while courier_loop:
                display_menu_courier()
                courier_input = int(input('Choose an Option: '))
                if courier_input == 0:
                    courier_loop = False
                elif courier_input == 1:
                    display_courier_list()
                elif courier_input == 2:
                    create_new_courier()
                elif courier_input == 3:
                    update_existing_courier()
                elif courier_input == 4:
                    delete_courier()
                else:
                    print("Invalid option. Please try again.")
        elif user_input == 3:
            order_loop = True
            while order_loop:
                display_menu_order()
                order_input = int(input('Choose an Option: '))

                if order_input == 0:
                    order_loop = False
                elif order_input == 1:
                    display_customer_order()
                elif order_input == 2:
                    create_new_order()
                elif order_input == 3:
                    update_existing_order_status()
                elif order_input == 4:
                    update_existing_order()
                elif order_input == 5:
                    delete_order()
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid option. Please choose a valid option.")


# Run the main function
main()