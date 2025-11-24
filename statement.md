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



---

🎯 Target Users

The Supermarket Billing & Inventory Management System is designed for the following groups of users:


1. Small and Medium Supermarket Owners

Owners who need a simple tool for managing billing and inventory.

Helps them reduce manual calculation errors.

Useful for stores without advanced POS systems.



2. Cashiers and Billing Staff

People responsible for daily billing tasks.

Can use this system to quickly:

Add items

Generate bills

Apply discounts

Provide receipts to customers



3. Students Learning Python

Ideal for beginners who want to understand:

Dictionaries

File handling

Functions

Loops

Basic inventory logic


A great educational project for practice and assignments.



4. Developers Creating Billing Systems

Programmers who want a base model to build:

A GUI billing application

A web-based shopping portal

Mobile shopping systems



5. Training Institutes / Schools

Useful for teaching:

Project-based learning

Logic building

Real-world application development


Can be used as a demonstrative project in labs.



6. Freelancers / Shop Assistants

People helping local shops can use it to streamline billing.

Saves time by automating calculations.



---

⭐ High-Level Features

1. Product Inventory Management

Maintains a list of available supermarket items along with their prices and stock levels, and updates stock automatically based on user actions.



2. Shopping Cart System

Allows users to add and remove items, manage quantities, and view real-time cart contents before checkout.




3. Automated Billing & Price Calculation

Generates a complete bill that includes:

Item name

Quantity

Unit price

Subtotal per item

Grand total


All calculations are automatic and error-free.



4. Coupon / Discount Handling

Supports discount codes (e.g., SAVE10) to reduce the total bill.
The system validates the coupon and applies the correct discount percentage.



5. Receipt Generation

Automatically creates a detailed receipt in a .txt file containing:

Customer details

Order ID

Purchased items

Final payable amount

Delivery address

Estimated delivery date



6. User-Friendly Menu Interface

A clean, menu-driven interface that lets users:

View all items

Add / remove products

Checkout

Exit the system easily



7. Order and Delivery Simulation

Generates:

A unique random Order ID

An estimated delivery date based on the current date and random delivery days


This simulates the online shopping experience.



8. Error Handling & Input Validation

Handles:

Invalid item names

Out-of-stock conditions

Invalid quantity removal

Wrong coupon codes


Ensures smooth and safe user experience.


