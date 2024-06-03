import pandas as pd
from pathlib import Path
from datetime import datetime

#Get the path of the file 'inventory.csv'
# Name of the CSV file that stores the inventory data
csv_file = Path(__file__).parent / 'inventory.csv'

# Function to read the CSV file and return a DataFrame
def read_inventory():
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame with the necessary columns
        df = pd.DataFrame(columns=['id', 'name', 'quantity', 'price'])
    return df

# Function to save the DataFrame to the CSV file
def save_inventory(df):
    df.to_csv(csv_file, index=False)

# Function to display the current inventory
def display_inventory():
    df = read_inventory()
    print(df)

# Function to get information from user to use in add_product function
def get_information_to_add_product():
    id = input("Product ID: ")
    name = input("Product name: ")
    quantity = int(input("Product quantity: "))
    min_quantity = int(input("Minimum Quantity: "))
    max_quantity = int(input("Maximum Quantity: "))
    supplier = input("Supplier: ")
    manufacturer = input("Manufacturer: ")
    price = float(input("Product price: "))
    return [id, name, quantity, min_quantity, max_quantity, supplier, manufacturer, price]

# Function to add a new product
def add_product(id, name, quantity, min_quantity, max_quantity, price, supplier, manufacturer):
    now = datetime.now()
    df = read_inventory()
    new_product = pd.DataFrame([[id, name, quantity, min_quantity, max_quantity, price, supplier, manufacturer, now]], columns=['id', 'name', 'quantity', 'min_quantity', 'max_quantity', 'price', 'supplier', 'manufacturer', 'last_movimentation'])
    df = pd.concat([df, new_product], ignore_index=True)
    save_inventory(df)
    print(f"Product '{name}' added successfully!")

# Function to modify an existing product
def modify_product(id, name=None, quantity=None, price=None):
    df = read_inventory()

    if id in df['id'].astype(str).values:
        if name is not None:
            df.loc[df['id'] == id, 'name'] = name
        if quantity is not None:
            df.loc[df['id'] == id, 'quantity'] = quantity
        if price is not None:
            df.loc[df['id'] == id, 'price'] = price
        save_inventory(df)
        print(f"Product with ID {id} modified successfully!")
    else:
        print(f"Product with ID {id} not found.")

# Function to delete a product
def delete_product(id):
    df = read_inventory()
    if id in df['id'].astype(str).values:
        df = df[df['id'] != id]
        save_inventory(df)
        print(f"Product with ID {id} deleted successfully!")
    else:
        print(f"Product with ID {id} not found.")

# Inventory control system menu
def manage_menu(choice):
    if choice == '1':
        display_inventory()
    elif choice == '2':
        product = get_information_to_add_product()
        id, name, quantity, min_quantity, max_quantity, supplier, manufacturer, price = product 
        add_product(id, name, quantity, min_quantity, max_quantity, price, supplier, manufacturer)
    elif choice == '3':
        id = input("ID of the product to modify: ")
        name = input("New product name (leave blank if not changing): ")
        quantity = input("New product quantity (leave blank if not changing): ")

        price = input("New product price (leave blank if not changing): ")
        
        name = name if name else None
        quantity = int(quantity) if quantity else None
        price = float(price) if price else None

        modify_product(id, name, quantity, price)
    elif choice == '4':
        id = input("ID of the product to delete: ")
        delete_product(id)
    elif choice == '5':
        print("Exiting the system...")
        return False
    else:
        print("Invalid option. Please try again.")

def main():
    while True:
        print("\nInventory Control System")

        print("1. Search Product")
        print("2. Calculate the inventory value")
        print("3. Check the inventory")
        print("4. Manage products")
        print("5. Exit")

        navegation = input("Choose an option: ")
        
        match navegation:
            case '1':
                print("Search Product")
            case '2':
                print("Calculate the inventory value")
            case '3':
                print("Check the inventory")
            case '4':
                while True:
                    print("\nInventory Control System")
                    print("1. Display inventory")
                    print("2. Add product")
                    print("3. Modify product")
                    print("4. Delete product")
                    print("5. Exit")
                    choice = input("Choose an option: ")
                    # Run the menu
                    if manage_menu(choice) == False:
                        break
            case _: 
                print("5. Exit")
                break
        

if __name__ == '__main__':
    main()
