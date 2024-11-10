from create_connection import cursor
from create_connection import conn

# Load Data  From couriers table in Database
def load_couriers_from_db():
    cursor.execute("SELECT courier_name, courier_phone_number FROM couriers")
    couriers = cursor.fetchall()
    return [{'courier_name': row[0], 'courier_phone_number': row[1]} for row in couriers]

def save_couriers_to_db():
    # Clear Table before saving Data Into the Database
    cursor.execute("DELETE FROM couriers")
    for courier in couriers:
        cursor.execute(
            "INSERT INTO couriers (courier_name, courier_phone_number) VALUES (%s, %s)",
            (courier['courier_name'], courier['courier_phone_number'])
        )
    conn.commit()

couriers = load_couriers_from_db()

# Display Courier List
def display_courier_list():
    print("Courier List:")
    print('-' *50)

    for i, courier in enumerate(couriers):
        print(f"Courier {i + 1} Name: {courier['courier_name']} - Phone Number: {courier['courier_phone_number']}")
    print('-' *50)

# Create New Courier
def create_new_courier():
    courier_name = input('Enter the courier name: ')
    courier_phone_number = input('Enter the courier number: ')

    new_courier = {
        'courier_name': courier_name,
        'courier_phone_number': courier_phone_number
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
            confirm_delete_courier = input(f"Are you sure you want to delete {couriers[courier_index]['courier_name']} ? (yes/no):  ")
            if confirm_delete_courier.lower() == 'yes':
                couriers.pop(courier_index)
                print(f"Courier deleted successfully.")
        else:
            print("Invalid courier number.")
    except ValueError:
        print("Please enter a valid number.")
