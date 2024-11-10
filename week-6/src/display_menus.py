# Main Menu
menu_options = ['Exit App', 'Print Products Menu', 'Print Couriers Menu', 'Print Orders Menu']

# Products Menu
products_menu = ['Return to Main Menu', 'Print Products List', 'Add new Product', 'Update Existing Product', 'Delete Product']

# Orders Menu
orders_menu = ['Return to Main Menu', 'Print Customer Order', 'Create New Order', 'Update Existing Order Status', 'Update Existing Order', 'Delete Order']

# Couriers Menu
couriers_menu = ['Return to Main Menu', 'Print Courier List', 'Create New Courier', 'Update Existing Courier', 'Delete Courier']

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

# Display Menu Courier
def display_menu_courier():
    print('Couriers Menu')
    for i, option in enumerate(couriers_menu):
        print(f'{i} : {option}')
    print()

# Display Menu Order
def display_menu_order():
    print("Orders Menu:")
    for i, option in enumerate(orders_menu):
        print(f"{i} : {option}")
    print("-" *50)
