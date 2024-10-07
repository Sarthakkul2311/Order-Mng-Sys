import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.OrderProcessor import OrderProcessor
from entity.User import User
from entity.Electronics import Electronics
from entity.Clothing import Clothing
from exception.UserNotFound import UserNotFound
from exception.OrderNotFound import OrderNotFound

def main_menu():
    order_processor = OrderProcessor()

    while True:
        print("\nOrder Management System")
        print("1. Create User")
        print("2. Create Product (Admin Only)")
        print("3. Get All Products")
        print("4. Create Order")
        print("5. Cancel Order")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                userId = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ").capitalize()
                user = User(userId, username, password, role)
                order_processor.createUser(user)
            except Exception as e:
                print(f"Error creating user: {e}")

        elif choice == '2':
            try:
                userId = int(input("Enter Admin User ID: "))
                user = order_processor.getUserById(userId)

                if user and user.role == "Admin":
                    productId = int(input("Enter Product ID: "))
                    productName = input("Enter Product Name: ")
                    description = input("Enter Description: ")
                    price = float(input("Enter Price: "))
                    quantityInStock = int(input("Enter Quantity in Stock: "))
                    product_type = input("Enter Type (Electronics/Clothing): ").capitalize()

                    if product_type == "Electronics":
                        brand = input("Enter Brand: ")
                        warrantyPeriod = int(input("Enter Warranty Period: "))
                        product = Electronics(productId, productName, description, price, quantityInStock, brand, warrantyPeriod)
                    elif product_type == "Clothing":
                        size = input("Enter Size: ")
                        color = input("Enter Color: ")
                        product = Clothing(productId, productName, description, price, quantityInStock, size, color)
                    else:
                        print("Invalid product type. Please enter 'Electronics' or 'Clothing'.")
                        continue
                    
                    order_processor.createProduct(user, product)
                    print("Product created successfully!")
                else:
                    print("Only Admin users can create products.")
            except UserNotFound as e:
                print(e)
            except Exception as e:
                print(f"Error creating product: {e}")

        elif choice == '3':
            try:
                products = order_processor.getAllProducts()
                if products:
                    for product in products:
                        print(f"Product ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, "
                              f"Price: {product[3]}, Quantity in Stock: {product[4]}, Type: {product[5]}")
                else:
                    print("No products available.")
            except Exception as e:
                print(f"Error fetching products: {e}")

        elif choice == '4':  # Create Order
            try:
                userId = int(input("Enter User ID: "))
                user = order_processor.getUserById(userId)

                if not user:
                    print(f"User with ID {userId} does not exist.")
                    continue

                products = order_processor.getAllProducts()
                if not products:
                    print("No products available for order.")
                    continue

                # Display available products
                print("Available Products:")
                for product in products:
                    print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[3]}, Quantity in Stock: {product[4]}")

                # User selects products
                selected_products = []
                while True:
                    productId = int(input("Enter Product ID to add to order (0 to stop): "))
                    if productId == 0:
                        break

                    # Fetch product details based on productId
                    product = next((p for p in products if p[0] == productId), None)
                    if not product:
                        print("Invalid Product ID. Please try again.")
                        continue

                    quantity = int(input(f"Enter quantity for {product[1]} (Available: {product[4]}): "))
                    if quantity > product[4]:
                        print(f"Insufficient stock for {product[1]}. Only {product[4]} available.")
                        continue

                    selected_products.append((productId, quantity))

                if selected_products:
                    # Proceed to create the order
                    order_processor.createOrder(user, selected_products)
                    print("Order created successfully!")
                else:
                    print("No products selected for the order.")
            except Exception as e:
                print(f"Error creating order: {e}")

        elif choice == '5':
            # Cancel Order functionality
            try:
                userId = int(input("Enter User ID: "))
                user = order_processor.getUserById(userId)

                if not user:
                    print(f"User with ID {userId} does not exist.")
                    continue

                orderId = int(input("Enter Order ID to cancel: "))
                order_processor.cancelOrder(userId, orderId)
            except OrderNotFound as e:
                print(e)
            except Exception as e:
                print(f"Error cancelling order: {e}")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
