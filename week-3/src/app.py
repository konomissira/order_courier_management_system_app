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

def save_products():
    with open("../data/convert_to_csv/products_list.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for product in products_list:
            writer.writerow([product])  # Write each product as a single row


def save_couriers():
    with open("../data/week-3/data/convert_to_csv/couriers_list.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for courier in couriers:
            writer.writerow([courier])  # Write each courier as a single row

def save_orders():
    with open("../data/week-3/data/convert_to_csv/orders.csv", "w", newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["customer_name", "customer_address", "customer_phone", "status", "items"])
        
        for order in orders:
            items_str = ";".join([f"{item['name']}:{item['quantity']}" for item in order['items']])
            writer.writerow([order["customer_name"], order["customer_address"], order["customer_phone"], order["status"], items_str])


# Main Menu
menu_options = ['Exit App', 'Print Products Menu', 'Print Couriers Menu', 'Print Orders Menu']

# Products Menu
products_menu = ['Return to Main Menu', 'Print Products List', 'Add new Product', 'Update Existing Product', 'Delete Product']

# Orders Menu
orders_menu = ['Return to Main Menu', 'Print Customer Order', 'Create New Order', 'Update Existing Order Status', 'Update Existing Order', 'Delete Order']

# Couriers Menu
couriers_menu = ['Return to Main Menu', 'Print Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']

# Load data from files
couriers = read_file('../data/couriers.txt')
products_list = read_file('../data/products_list.txt')
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
    print('****************************************')

# Display Menu Order
def display_menu_order():
    print("Orders Menu:")
    for i, option in enumerate(orders_menu):
        print(f"{i} : {option}")
    print('****************************************')

# Display Product List
def display_product_list():
    print("Products List:")
    for product in products_list:
        print(product)
    print()

# Add New Product
def add_new_product():
    new_product = input('Enter the product name to be added: ')
    products_list.append(new_product)
    print(f"Product '{new_product}' added successfully!")

# Update Existing Product
def update_existing_product():
        for i, product in enumerate(products_list):
            print(f"{i} : {product}")
        product_index = int(input('Choose product index to be edited: '))
        new_name = input('Enter new name: ')
        products_list[product_index] = new_name
        print(f"Product updated to: {new_name}")

# Delete Product
def delete_product():
    for i, product in enumerate(products_list):
        print(f"{i} : {product}")
    product_name = input('Enter the product name to delete: ')
    if product_name in products_list:
        products_list.remove(product_name)
        print(f"Product '{product_name}' deleted successfully!")
    else:
        print(f"Product '{product_name}' not found.")

# Display Menu Courier
def display_menu_courier():
    print('Couriers Menu')
    for i, option in enumerate(couriers_menu):
        print(f'{i} : {option}')
    print()

# Display Courier List
def display_courier_list():
    print("Courier List:")
    for i, courier in enumerate(couriers):
        print(f"{i + 1}: {courier}")
    print()

# Create New Courier
def create_new_courier():
    new_courier = input("Enter the name of the new courier: ").strip()
    if new_courier:
        couriers.append(new_courier)
        print(f"Courier '{new_courier}' added successfully.")
    else:
        print("Courier name cannot be empty.")

# Update Existing Courier
def update_existing_courier():
    display_courier_list()
    try:
        courier_index = int(input("Enter the courier number to update: ")) - 1
        if 0 <= courier_index < len(couriers):
            new_name = input("Enter the new name for the courier: ").strip()
            if new_name:
                couriers[courier_index] = new_name
                print(f"Courier updated to '{new_name}'.")
            else:
                print("Courier name cannot be empty.")
        else:
            print("Invalid courier number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete Courier
def delete_courier():
    display_courier_list()
    try:
        courier_index = int(input("Enter the courier number to delete: ")) - 1
        if 0 <= courier_index < len(couriers):
            deleted_courier = couriers.pop(courier_index)
            print(f"Courier '{deleted_courier}' deleted successfully.")
        else:
            print("Invalid courier number.")
    except ValueError:
        print("Please enter a valid number.")

# Display Customer Order
def display_customer_order():
    print("Customer Orders:")
    for order in orders:
        print(f"Customer Name: {order['customer_name']}")
        print(f"Address: {order['customer_address']}")
        print(f"Phone: {order['customer_phone']}")
        print(f"Status: {order['status']}")
        print("Items:")
        for item in order['items']:
            print(f"  - {item['name']} x {item['quantity']}")
        print()

# Create New Order
def create_new_order():
    customer_name = input("Enter the customer's name: ")
    customer_address = input("Enter the customer's address: ")
    customer_phone = input("Enter the customer's phone number: ")
    
    order_items = []
    while True:
        item_name = input("Enter an item (or type 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        
        item_quantity = int(input(f"Enter the quantity for {item_name}: "))
        order_items.append({'name': item_name, 'quantity': item_quantity})

    new_order = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "status": "preparing",
        "items": order_items
    }
    
    orders.append(new_order)  # Add the new order to the list
    print(f"New order created successfully for {customer_name}.")

# Update Order Status
def update_order_status():
    if not orders:
        print("No orders available to update.")
        return

    print("Existing Orders:")
    for i, order in enumerate(orders):
        print(f"Order {i + 1}: {order['customer_name']} (Status: {order['status']})")

    try:
        order_index = int(input("Enter the order number to update the status: ")) - 1  # Adjust for 0-based index

        if 0 <= order_index < len(orders):
            new_status = input("Enter the new status (e.g., preparing, completed, cancelled): ")
            orders[order_index]['status'] = new_status  # Update the status
            print(f"Order {orders[order_index]['customer_name']}'s status updated to '{new_status}'.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Update Existing Order
def update_existing_order():
    if not orders:
        print("No orders available to update.")
        return

    print("Existing Orders:")
    for i, order in enumerate(orders):
        print(f"Order {i + 1}: {order['customer_name']} (Status: {order['status']})")

    try:
        order_index = int(input("Enter the order number to update: ")) - 1  # Adjust for 0-based index

        if 0 <= order_index < len(orders):
            # Update customer details if needed
            update_choice = input("Do you want to update customer details (yes/no)? ").strip().lower()
            if update_choice == 'yes':
                orders[order_index]['customer_name'] = input("Enter the new customer's name: ")
                orders[order_index]['customer_address'] = input("Enter the new customer's address: ")
                orders[order_index]['customer_phone'] = input("Enter the new customer's phone number: ")

            # Update status
            new_status = input("Enter the new status (e.g., preparing, completed, cancelled): ")
            orders[order_index]['status'] = new_status

            # Update items
            item_update_choice = input("Do you want to update items (yes/no)? ").strip().lower()
            if item_update_choice == 'yes':
                order_items = orders[order_index]['items']
                while True:
                    print("Current items:")
                    for j, item in enumerate(order_items):
                        print(f"  {j + 1}: {item['name']} (x{item['quantity']})")
                    
                    item_choice = int(input("Enter the item number to update or type 0 to add a new item: ")) - 1

                    if item_choice == -1:
                        # Add new item
                        item_name = input("Enter the name of the new item: ")
                        item_quantity = int(input("Enter the quantity for the new item: "))
                        order_items.append({'name': item_name, 'quantity': item_quantity})
                    elif 0 <= item_choice < len(order_items):
                        # Update existing item
                        new_quantity = int(input(f"Enter the new quantity for {order_items[item_choice]['name']}: "))
                        order_items[item_choice]['quantity'] = new_quantity
                    else:
                        print("Invalid item number.")
                    
                    continue_choice = input("Do you want to update another item (yes/no)? ").strip().lower()
                    if continue_choice != 'yes':
                        break

            print(f"Order {orders[order_index]['customer_name']}'s details updated successfully.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete order
def delete_order():
    if not orders:
        print("No orders to delete.")
        return

    print("Existing Orders:")
    for i, order in enumerate(orders):
        print(f"Order {i + 1}: {order['customer_name']} (Status: {order['status']})")

    try:
        order_index = int(input("Enter the order number to delete: ")) - 1
        if 0 <= order_index < len(orders):
            deleted_order = orders.pop(order_index)
            print(f"Deleted order for {deleted_order['customer_name']}.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Invalid input.")


# Main app loop
def main():
    do_loop = True

    while do_loop:
        display_main_menu()
        print("0 : Exit")
        print("1 : Exit")
        print("2 : Exit")
        user_input = int(input('Choose an Option: '))

        if user_input == 0:
            # Save data to files
            write_file('../data/couriers.txt', couriers)
            write_file('../data/products_list.txt', products_list)
            write_json('../data/orders.json', orders)
            save_products()
            
            print("Exiting app... Data saved.")
            do_loop = False
        elif user_input == 1:
            product_loop = True
            while product_loop:
                display_menu_product()
                product_input = int(input('Choose an Option: '))

                if product_input == 0:
                    product_loop = False
                elif product_input == 1:
                    display_product_list()
                elif product_input == 2:
                    # new_product = input('Enter the product name to be added: ')
                    # products_list.append(new_product)
                    # print(f"Product '{new_product}' added successfully!")
                    add_new_product()
                elif product_input == 3:
                    # for i, product in enumerate(products_list):
                    #     print(f"{i} : {product}")
                    # product_index = int(input('Choose product index to be edited: '))
                    # new_name = input('Enter new name: ')
                    # products_list[product_index] = new_name
                    # print(f"Product updated to: {new_name}")
                    update_existing_product()
                elif product_input == 4:
                    # for i, product in enumerate(products_list):
                    #     print(f"{i} : {product}")
                    # product_name = input('Enter the product name to delete: ')
                    # if product_name in products_list:
                    #     products_list.remove(product_name)
                    #     print(f"Product '{product_name}' deleted successfully!")
                    # else:
                    #     print(f"Product '{product_name}' not found.")
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
                    update_order_status()
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