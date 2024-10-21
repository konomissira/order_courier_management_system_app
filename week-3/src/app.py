# Main Menu
menu_options = ['Exit App', 'Print Products Menu', 'Print Orders Menu', 'Print Couriers Menu']

# Products Menu
products_menu = ['Return to Main Menu', 'Print Products List', 'Add new Product', 'Update Existing Product', 'Delete Product']

# Orders Menu
orders_menu = ['Return to Main Menu', 'Print Customer Order', 'Create New Order', 'Update Existing Order Status', 'Update Existing Order', 'Delete Order']

# Couriers Menu
couriers_menu = ['Return to Main Menu', 'Print Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']

# Products List
#products_list = ['Latte', 'Mocha', 'Hot Chocolate', 'English Breakfast Tea']

# Courier List
#couriers = ['Yodel', 'DHL', 'DPD']

# Order List
orders = [
    {
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, somewhere",
        "customer_phone": "0300000099",
        "status": "preparing",
        "items": [{'name': 'Tuna Toast', 'quantity': 1}, {'name': 'Americano', 'quantity': 2}]
    },
    {
        "customer_name": "Jane",
        "customer_address": "123 Elm Street",
        "customer_phone": "0400000011",
        "status": "completed",
        "items": [{'name': 'Hot Chocolate', 'quantity': 1}]
    }
]

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

# Display Menu Courier
def display_menu_courier():
    print('Couriers Menu')
    for i, option in enumerate(couriers_menu):
        print(f'{i} : {option}')
    print()

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

def main():
    do_loop = True

    while do_loop:
        display_main_menu()
        user_input = int(input('Choose an Option: '))

        if user_input == 0:
            print("Exiting app...")
            do_loop = False
        elif user_input == 1:
            product_loop = True
            while product_loop:
                display_menu_product()
                product_input = int(input('Choose an Option: '))

                if product_input == 0:
                    product_loop = False
                elif product_input == 1:
                    print("Products List:")
                    ####################################
                    file = open("../data/products_list.txt", "r")
                    lines = file.readlines()
                    for line in lines:
                        print(line)
                    ####################################
                    # for product in products_list:
                    #     print(product)
                    # print()
                elif product_input == 2:
                    new_product = input('Enter the product name to be added: ')
                    products_list.append(new_product)
                    print(f"Product '{new_product}' added successfully!")
                elif product_input == 3:
                    for i, product in enumerate(products_list):
                        print(f"{i} : {product}")
                    product_index = int(input('Choose product index to be edited: '))
                    new_name = input('Enter new name: ')
                    products_list[product_index] = new_name
                    print(f"Product updated to: {new_name}")
                elif product_input == 4:
                    for i, product in enumerate(products_list):
                        print(f"{i} : {product}")
                    product_name = input('Enter the product name to delete: ')
                    if product_name in products_list:
                        products_list.remove(product_name)
                        print(f"Product '{product_name}' deleted successfully!")
                    else:
                        print(f"Product '{product_name}' not found.")
                else:
                    print("Invalid option. Please try again.")
        elif user_input == 2:
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
        elif user_input == 3:
            courier_loop = True
            while courier_loop:
                display_menu_courier()
                courier_input = int(input('Choose an Option: '))
                if courier_input == 0:
                    courier_loop = False
                elif courier_input == 1:
                    pass
                elif courier_input == 2:
                    pass
                elif courier_input == 3:
                    pass
                elif courier_input == 4:
                    pass
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid option. Please choose a valid option.")

main()