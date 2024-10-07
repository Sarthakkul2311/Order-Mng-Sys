from util.DBUtil import DBUtil
from exception.UserNotFound import UserNotFound
from exception.OrderNotFound import OrderNotFound
from dao.IOrderManagementRepository import IOrderManagementRepository
from entity.User import User

class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.conn = DBUtil.getDBConn()

    # Create a new user in the database
    def createUser(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                           user.userId, user.username, user.password, user.role)
            self.conn.commit()
            print("User created successfully!")
        except Exception as e:
            print(f"Error creating user: {e}")

    # Retrieve a user by their ID
    def getUserById(self, userId):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE userId = ?", userId)
            user_data = cursor.fetchone()
            if user_data is None:
                raise UserNotFound(f"User with ID {userId} not found.")
            user = User(user_data[0], user_data[1], user_data[2], user_data[3])
            return user
        except UserNotFound as e:
            print(e)
            return None
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None

    # Create an order for the user, updating stock and inserting records into Orders
    def createOrder(self, user, selected_products):
        try:
            cursor = self.conn.cursor()
            for productId, quantity in selected_products:
                # Check stock for each product
                cursor.execute("SELECT quantityInStock FROM Products WHERE productId = ?", productId)
                stock = cursor.fetchone()
                if stock is None or stock[0] < quantity:
                    raise Exception(f"Insufficient stock for product ID {productId}. Available: {stock[0]}.")

                # Deduct stock and add product to order
                cursor.execute("UPDATE Products SET quantityInStock = quantityInStock - ? WHERE productId = ?", quantity, productId)
                cursor.execute("INSERT INTO Orders (userId, productId, quantity) VALUES (?, ?, ?)", user.userId, productId, quantity)

            self.conn.commit()
            print("Order created successfully!")
        except Exception as e:
            print(f"Error creating order: {e}")
            self.conn.rollback()

    # Cancel an order by removing it from the Orders table and updating stock
    def cancelOrder(self, userId, orderId):
        try:
            cursor = self.conn.cursor()

            # Check if the order exists
            cursor.execute("SELECT productId, quantity FROM Orders WHERE orderId = ? AND userId = ?", orderId, userId)
            order_items = cursor.fetchall()
            
            if len(order_items) == 0:
                raise OrderNotFound(f"Order with ID {orderId} not found for user {userId}.")

            # Revert the stock for the products in the order
            for productId, quantity in order_items:
                cursor.execute("UPDATE Products SET quantityInStock = quantityInStock + ? WHERE productId = ?", quantity, productId)

            # Delete the order after stock update
            cursor.execute("DELETE FROM Orders WHERE orderId = ? AND userId = ?", orderId, userId)
            self.conn.commit()
            print(f"Order ID {orderId} for user {userId} has been cancelled and stock has been updated.")
        
        except OrderNotFound as e:
            print(e)
        except Exception as e:
            print(f"Error cancelling order: {e}")
            self.conn.rollback()

    # Create a new product in the database (admin users only)
    def createProduct(self, user, product):
        try:
            if user.role != "Admin":
                raise PermissionError("Only Admin users can create products.")

            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Products (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                           product.productId, product.productName, product.description, product.price, product.quantityInStock, product.type)

            if product.type == "Electronics":
                cursor.execute("INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES (?, ?, ?)",
                               product.productId, product.brand, product.warrantyPeriod)
            elif product.type == "Clothing":
                cursor.execute("INSERT INTO Clothing (productId, size, color) VALUES (?, ?, ?)",
                               product.productId, product.size, product.color)

            self.conn.commit()
            print("Product created successfully!")
        except PermissionError as e:
            print(e)
        except Exception as e:
            print(f"Error creating product: {e}")

    # Retrieve all products from the database
    def getAllProducts(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Products")
            products = cursor.fetchall()

            # Convert product data into a list of tuples
            product_list = []
            for product in products:
                product_data = (
                    product[0],  # productId
                    product[1],  # productName
                    product[2],  # description
                    float(product[3]),  # price (convert Decimal to float)
                    product[4],  # quantityInStock
                    product[5]   # type
                )
                product_list.append(product_data)

            return product_list
        except Exception as e:
            print(f"Error fetching products: {e}")

    # Retrieve all orders by a user
    def getOrderByUser(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Orders WHERE userId = ?", user.userId)
            orders = cursor.fetchall()
            return orders
        except Exception as e:
            print(f"Error fetching orders: {e}")
