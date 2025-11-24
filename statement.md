📌 Problem Statement

Managing supermarket billing, inventory, and customer orders manually is time-consuming, error-prone, and inefficient. Supermarkets and grocery stores need a simple system that can:

Display available products with real-time stock

Allow customers to select items and purchase them

Handle cart operations (add/remove)

Automatically update inventory

Calculate total bills accurately

Apply discounts or coupons

Generate a proper receipt

Record customer details and order information


Without such a system, mistakes can occur in stock management, billing calculations, and customer order processing. A simple, user-friendly digital solution is needed to automate these tasks.

---

📘 Scope of the Project

The Supermarket Billing & Inventory Management System focuses on providing a simple and efficient way to manage supermarket shopping operations through a console-based Python application. The scope of this project includes the following:


1. Product Inventory Management

The system maintains a list of 30 predefined products.

Each product has:

Name

Price

Available stock

Stock is updated automatically when items are added or removed from the cart.



2. Shopping Cart Functionality

Users can add multiple items to the cart.

Users can remove items or adjust quantities.

The system tracks:

Item names

Quantities

Total cost


Prevents adding more items than available in stock.


3. Billing and Checkout

Displays a complete bill with:

Item names

Quantity purchased

Unit price

Subtotal


Calculates grand total automatically.

Supports coupon code application (e.g., SAVE10).


4. Receipt Generation

Saves a detailed receipt as a text file.

Receipt includes:

Customer name

Order ID

Items and totals

Delivery address

Expected delivery date


5. User Interaction Through Menu

Users can:

1. View items


2. Add to cart


3. Remove from cart


4. Checkout


5. Exit



Inputs are handled using a simple console interface.


6. Order and Delivery Simulation

Random Order ID generator.

Random estimated delivery date.

Enhances realism of the shopping experience.


7. Basic Error Handling

Prevents invalid item selection.

Prevents negative or excessive quantities.

Handles missing or incorrect coupon code entries.


