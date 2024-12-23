# Full-Stack Application for Coffee Shop:

A simple command-line application designed to manage products, couriers, and customer orders. The application provides an intuitive interface for users to create, update, view, and delete entries for products, couriers, and orders.

## Features

-   Product Management: Add, update, delete, and display product listings with names and prices.
-   Courier Management: Add, update, delete, and display couriers with names and phone numbers.
-   Order Management: Create new orders, update order status, modify existing orders, and delete orders.
-   Data Persistence: Save changes to a database for products, couriers, and orders to ensure data is preserved between sessions.

## Table of Contents:

-   Installation
-   Usage
-   Functions Overview
-   Error Handling
-   Testing
-   Project Reflections
-   License

### Installation:

-   This project is private, so in order to install it the permission of Generation UK is required. After permission from Generation UK. To install the application use the following git command to clone the project:

git clone https://github.com/generation-de-nat3/mahamadou_miniproject.git

-   Install dependencies: To install depencies running the following command:
    -   pip install -r requirements.txt
-   Set up the database:
    Configure a PostgreSQL database and update the connection details in the code as required.

    Note: This project uses PostgreSQL and Pgadmin

### Usage:

This project was built on weekly goal over six weeks rows. So to run the final version of the project must be in week-6/src/database_management/ folder, then run the following:

-   python3 app_database.py

Note: Must start Docker Desktop and run: docker compose up -d. Because the application is relied on a Database Management System in this case PostgreSQL, it is necessary to create tables for products, couriers, and orders. There are two options to create tables:

-   Option 1: Using pgAdmin
    Open pgAdmin: Open your browser and go to http://localhost:8080 (the port I configured for pgAdmin).
    Login: Use the credentials you specified in your Docker Compose file.
    Connect to the PostgreSQL Server:
    In pgAdmin, right-click on “Servers” > “Create” > “Server.”
    Enter a name for your server.
    Go to the “Connection” tab and enter localhost as the hostname, 5432 as the port, and PostgreSQL credentials (name provided in Docker-compose file and the password).
    Open Query Tool:
    In the left sidebar, navigate to the database the Right-click on it and select “Query Tool.”
    Execute the following SQL Commands:

    CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL
    );

    CREATE TABLE couriers (
    id SERIAL PRIMARY KEY,
    courier_name VARCHAR(100),
    courier_phone_number VARCHAR(20)
    );

    CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_address VARCHAR(255),
    customer_phone VARCHAR(20),
    courier VARCHAR(100),
    status VARCHAR(50),
    items TEXT
    );

-   Option 2: Using psql Command-Line Tool
    Open Terminal: Open your terminal, access the PostgreSQL Container:
    Run the following command to enter into the PostgreSQL container:
    docker exec -it my_postgres_db psql -U your_username -d your_database. That command will take you to the database and from there it is possible to create table using SQL command.

Once running, from main menu you can access three submenus that manage respectively products, couriers, and orders:

-   Print Product Menu
-   Print Courier Menu
-   Print Order Menu

Each menu offers options to view, create, update, and delete products, couriers, and orders.

## Functions Overview:

### Main Functions

-   main(): The entry point of the application. Displays the main menu and directs the user to the appropriate section.
-   display_main_menu(): Displays the main menu options.

### Product Management

-   display_product_list(): Lists all available products.
-   create_new_product(): Prompts the user to add a new product with name and price validation.
-   update_existing_product(): Allows the user to update existing product details.
-   delete_product(): Removes a product after confirmation.

### Courier Management

-   display_courier_list(): Lists all available couriers.
-   create_new_courier(): Prompts the user to add a new courier with name and phone validation.
-   update_existing_courier(): Allows the user to update courier details.
-   delete_courier(): Removes a courier after confirmation.

### Order Management

-   display_orders(): Lists all orders along with their current statuses.
-   create_new_order(): Prompts the user for customer details, product selection, and courier assignment to create a new order.
-   update_existing_order(): Allows updating of various order fields including status.
-   update_existing_order_status(): Specifically updates the status of an order.
-   delete_order(): Removes an order after confirmation.

## Error Handling

The application check users' input for handling errors such as follows:

-   Input Validation: Ensures user inputs are within expected formats, e.g., numeric entries where required.
-   Range Checks: Prevents index out-of-bounds errors by checking if selections fall within valid ranges.
-   Confirmation Prompts: Ensures that deletions are confirmed to avoid accidental data loss.

## Testing:

To ensure the application is working correctly, automated tests have been written. Follow the steps below to run the tests:

-   Set Up Relative Imports: If you encounter errors like ModuleNotFoundError, make sure to use relative imports in the code. For example:
    Update imports in manage_orders_database.py, manage_products_database.py, and manage_couriers_database.py like this:
    from .manage_products_database import display_product_list, products_list
    from .manage_couriers_database import couriers
    from .manage_orders_database import orders

-   Install Dependencies: Running the following command:
    pip install -r requirements.txt

-   Run All Tests: Use pytest to run all tests in the tests folder:
    pytest

-   Run a Specific Test File: It is possible to run a specific test file, by using:
    pytest tests/test_manage_products_database.py

### Notes:

-   Ensure that the database and any necessary configurations (like .env files) are properly set up before running the tests.
-   Use pytest for testing since it is a powerful and widely-used testing framework for Python.
-   Always ensure the relative imports are configured correctly when testing within a project structure.

## Project Reflections:

-   Designed: the project is designed to be modular, with separate modules for managing products, couriers, and orders. This separation allowed to implement each feature independently, ensuring that the application meets its main requirements: adding, updating, deleting, and displaying information efficiently. Using a PostgreSQL database provided reliable data storage, meeting the requirement for data persistence.
-   Requirement: To guarantee the project’s requirements, automated tests was wrote using pytest on 2 functions: create a new product and create new courier functions. These tests validated those two functions. Additionally, input's validation was implemented to ensure that only valid data could be processed, preventing common user errors. Regular testing helped identify and address any bugs early on.
-   Future improvement: If I had more time, it would be good to add a graphical user interface using tkinter framework to make the application more user-friendly. It will be great as well to deploy the project.
-   Most challenging: The most challenging part of the project was implementing unit tests. Setting up effective tests required not only ensuring that each function behaved as expected but also dealing with import paths when working within a package structure. Using . before imports for relative paths was particularly tricky at first, as it caused errors until I fully understood the import structure within Python packages. After some troubleshooting and research, I was able to configure my imports correctly, which allowed my tests to run smoothly. This experience taught me a lot about Python’s module system and improved my problem-solving skills in debugging.

## License

This project is licensed under MIT License.
