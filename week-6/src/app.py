# Import Menus
from display_menus import display_main_menu
from display_menus import display_menu_product
from display_menus import display_menu_courier
from display_menus import display_menu_order

# Import Functions that Manage Products
from manage_products import display_product_list
from manage_products import create_new_product
from manage_products import update_existing_product
from manage_products import delete_product
from manage_products import save_products_list_to_csv

# Import Functions that Manage Couriers
from manage_couriers import display_courier_list
from manage_couriers import create_new_courier
from manage_couriers import update_existing_courier
from manage_couriers import delete_courier
from manage_couriers import save_courier_to_csv

# Import Functions that Manage Orders
from manage_orders import display_customer_order
from manage_orders import create_new_order
from manage_orders import update_existing_order_status
from manage_orders import update_existing_order
from manage_orders import delete_order
from manage_orders import save_orders_to_csv

# Main function
def main():
    do_loop = True

    while do_loop:
        display_main_menu()
        user_input = int(input('Choose an Option: '))

        if user_input == 0:
            # Save data to files
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