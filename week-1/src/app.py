products = ["Late", "Mocca", "English breakfast tea"]
main_menu = ["Exit", "Display the items", "Add Item", "Retreive Item", "Update Item", "Delete Item"]

do_loop = True

while(do_loop):
    print("0. Exit")
    print("1. Display the items")
    print("2. Add Item")
    print("3. Retreive Item")
    print("4. Update Item")
    print("5. Delete Item")

    user_input = int(input("Please, choose an option:  "))

    if(user_input == 0):
        do_loop = False
    elif(user_input == 1):
        print("**************************************")
        for (i, item) in enumerate(products):
            print(item)
    elif(user_input == 2):
        print(products)
        print("**************************************")
        product_name = input("Enter a product name to be add to the product list:  ")
        print("**************************************")
        add_item = products.append(product_name)
        print("Product added to the product list.")
        print("**************************************")
        for item in products:
            print(item)
    elif(user_input == 5):
        print("**************************************")
        # for item in products:
        #     print(item)
        for (i, item) in enumerate(main_menu):
            print(item)
        print("**************************************")
        item_name = input("Type the name of the item to be remove:  ")
        remove_item = products.remove(item_name)
        for item in products:
            print(item)
    print("**************************************")