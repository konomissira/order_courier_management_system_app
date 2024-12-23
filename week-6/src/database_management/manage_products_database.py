from .create_connection import cursor, conn

# Load Data  From products table in Database
def load_products_from_db():
    try:
        cursor.execute("SELECT product_name, product_price FROM products")
        products = cursor.fetchall()
        return [{'product_name': row[0], 'product_price': row[1]} for row in products]
    except Exception as e:
        print(f"An error occured while loading products: {e}")
        return []

def save_products_list_to_db():
    try:
        # Clear Table before saving Data Into the Database
        cursor.execute("DELETE FROM products")
        for product in products_list:
            cursor.execute(
                "INSERT INTO products (product_name, product_price) VALUES (%s, %s)",
                (product['product_name'], product['product_price'])
            )
        conn.commit()
        print("Products saved to database successfully.")
    except Exception as e:
        print(f"An error occured while saving products: {e}")

products_list = load_products_from_db()

def display_product_list():
    print("Products List:")
    print("-" * 50)
    for i, product in enumerate(products_list):
        print(f"Product{i + 1} {product['product_name']} : £{float(product['product_price']):.2f}")
    print('-' * 50)

# Create New Product
def create_new_product():
    while True:
        new_product_name = input('Enter the product name: ').strip()
        
        # Check if the product name is empty
        if not new_product_name:
            print("Product name cannot be empty. Please enter a valid name.")
            continue
        
        # Optional: Check if the length is within acceptable range
        if len(new_product_name) < 2 or len(new_product_name) > 50:
            print("Product name must be between 2 and 50 characters.")
            continue

        # Optional: Restrict special characters (only letters, numbers, spaces allowed)
        if not new_product_name.replace(" ", "").isalnum():
            print("Product name can only contain letters, numbers, and spaces.")
            continue

        break  # Exit loop if name passes all checks

    while True:
        try:
            new_product_price = float(input('Enter the product price: '))
            break
        except ValueError:
            print('Please enter a valid numeric value for the price.')

    new_product = {
        'product_name': new_product_name,
        'product_price': new_product_price
    }
    # Append New Product to product_list
    products_list.append(new_product)
    print(f'New product "{new_product_name}" added successfully.')



# Update Existing Product
def update_existing_product():
        display_product_list()
        try:
            product_index = int(input('Enter the product number to update: ')) - 1
            if 0 <= product_index < len(products_list):
                product_to_update = products_list[product_index]

                for key, value in product_to_update.items():
                    new_value = input(f"Enter new {key} (leave blank to keep '{value}'): ")
                    if new_value.strip():
                        if key == 'product_price':
                            try:
                                product_to_update[key] = float(new_value)
                            except ValueError:
                                print("Invalid input for price. Update canceled.")
                                return
                        else:
                            product_to_update[key] = new_value
                print('Product updated successfully')
            else:
                print('Invalid product number. Please enter a valid number from the list.')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

# Delete Product
def delete_product():
    display_product_list()

    try:
        remove_product = int(input('Enter the product number to delete: ')) - 1
        if 0 <= remove_product < len(products_list):
            to_confirm = input(f"Are you sure you want to delete {products_list[remove_product]['product_name']} ? (yes/no):  ")
            if to_confirm.lower() == 'yes':
                products_list.pop(remove_product)
                print("Product deleted successfully.")
            else:
                print('Deletion canceled.')
        else:
            print('Invalid input. Please, enter a valid number.')
    except ValueError:
        print('Invalid input. Please, enter a numeric value.')
