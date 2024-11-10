import csv

# Load CSV File Function
def load_csv(file_name):
    """Loads data from a CSV file and returns a list of dictionaries."""
    data = []
    try:
        with open(file_name, newline='') as file:
            reader = csv.DictReader(file)
            data.extend(row for row in reader)
    except FileNotFoundError:
        print(f"{file_name} not found.")
    return data

def save_products_list_to_csv():
    with open('../data/products_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['product_name', 'product_price'])

        for product in products_list:
            writer.writerow([product['product_name'], product['product_price']])

products_list = load_csv('../data/products_list.csv')

# Display Product List
def display_product_list():
    print("Products List:")
    print("-" * 50)
    for i, product in enumerate(products_list):
        print(f"Product{i + 1} {product['product_name']} : £{float(product['product_price']):.2f}")
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
        'product_name':new_product_name,
        'product_price':new_product_price
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
