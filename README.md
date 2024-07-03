

## Project Setup and Execution Instructions

### Cloning the Repository
To clone the repository containing the source code for ShopEasy, use the following command in your terminal:

```bash
git clone https://github.com/Zoyaaaaaaa/ShopEasy-Uplyft-.git
```

### Navigating to the Project Directory
Navigate to the project directory after cloning the repository:

```bash
cd ShopEasy-Uplyft-
```

### Running the Application
To run the ShopEasy Flask application, execute the `app.py` file using Python:

```bash
python main.py
```

### Accessing the Application
Once the application is running, access it in your web browser by visiting [http://localhost:5000](http://localhost:5000).

## Project Summary

### Overview
ShopEasy is a Flask-based web application designed to serve as an online store platform. It provides users with essential functionalities such as user authentication, product browsing, searching, and purchasing.

### Features
1. **User Authentication**: Users can register new accounts, log in securely, and log out when they're done.
2. **Product Search**: Users can search for products by name, enabling quick and easy access to desired items.
3. **Product Purchase**: Authenticated users can add products to their cart and proceed with the checkout process to make purchases.

### Technology Stack
The project utilizes the following technologies:

- **Python**: The primary programming language used for backend development.
- **Flask**: A lightweight web framework used to build the application.
- **SQLAlchemy**: A Python SQL toolkit and Object-Relational Mapping (ORM) library utilized for database management.
- **Flask-Login**: A Flask extension used for managing user sessions and authentication.
- **psutil**: A cross-platform library used to access system details, particularly utilized for the users module.

### Sample Queries and Results
The application facilitates the execution of various queries, including user registration, product search, and product purchase. Sample queries and their corresponding results can be demonstrated as follows:

1. **User Registration Query**:
   - Query: User registers with username "example_user" and password "example_password".
   - Result: User "example_user" successfully registered.

2. **Product Search Query**:
   - Query: User searches for products containing the keyword "mouse".
   - Result: List of products matching the search criteria is displayed, including "Wireless Mouse" and "Gaming Mouse Pad".

3. **Product Purchase Query**:
   - Query: Authenticated user purchases the "Wireless Mouse".
   - Result: The "Wireless Mouse" product is added to the user's cart and deducted from the available stock.

## Conclusion
ShopEasy offers a user-friendly and efficient online shopping experience with its intuitive interface and robust functionalities. Leveraging Flask and associated libraries, the application provides essential features required for an online store platform, catering to both users and administrators alike. With its clean design and seamless execution, ShopEasy stands as a testament to the power and versatility of Flask in web development.
