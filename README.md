# Order Management System

This project implements a simple Order Management System using Python and MS SQL connectivity. The system allows users to create accounts, manage products, place orders, and cancel orders.

## Features

- User management (create user, retrieve user)
- Product management (create product, retrieve products)
- Order management (create order, retrieve orders, cancel order)
- Role-based access control (Admin and User)

## Technologies Used

- Python
- MS SQL Server
- Object-Oriented Programming (OOP)
- Exception Handling
- Collections

## Directory Structure
│
├── /dao
│   ├── __init__.py
│   └── OrderProcessor.py
|   └── IOrderManagementRepository.py
│
├── /entity
│   ├── __init__.py
│   └── User.py
│   └── Electronics.py
│   └── Clothing.py
|   └── Product.py
│
├── /exception
│   ├── __init__.py
│   └── UserNotFound.py
│   └── OrderNotFound.py
│
├── /util
│   ├── __init__.py
│   └── DBPropertyUtil.py
|   └── DBUtil.py
│
└── /main
    ├── __init__.py
    └── MainModule.py


### 1. `dao/` 
Contains the data access objects for managing users, products, and orders.

### 2. `entity/` 
Contains the data models representing users, products, electronics, and clothing.

### 3. `exception/` 
Contains custom exception classes for user and order not found scenarios.

### 4. `util/` 
Contains utility functions, including database connection management.

### 5. `main.py` 
The entry point for the application, implementing the menu-driven interface.

## Setup and Installation

### Prerequisites

- Python 3.x
- MS SQL Server
- Required Python libraries 

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <https://github.com/Sarthakkul2311/Order-Mng-Sys.git>
   cd OrderManagementSystem

2. Install required libraries:
       pip install pyodbc

3. Update the database connection details in DBUtil.py to connect to your MS SQL Server.

4. Run the application:
       python MainModule.py
   
## Author
### Sarthak Kulkarni
