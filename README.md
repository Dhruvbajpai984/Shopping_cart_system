#Shopping_cart_system
Project Overview: Supermarket Billing & Inventory Management System (Python)

This Python project is a console-based supermarket shopping and billing system that allows customers to browse products, add items to their cart, remove items, apply discounts, and generate a detailed receipt. The program also includes an inventory system that tracks stock levels in real time.

The application simulates a real-world online shopping experience, including login, product lists, cart management, billing, coupon system, and automatic receipt generation.



Key Features of the Project

1. Login System

Welcomes the user with their entered name.

Makes the system feel personalized.


2. Product Inventory (30 Items)
 
A dictionary stores 30 grocery items with:

Price

Stock availability


Updates stock automatically when the user buys or removes items.



---

3. Display Items Function

Shows all available items in a neat format.

Displays:

Item Name

Price

Current Stock




---

4. Add-to-Cart System

User can add items by name.

Quantity can be selected.

Automatically checks:

If item exists

If stock is sufficient


Reduces inventory when items are added.

Stores:

Item names

Corresponding prices


Allows adding multiple quantities at once.



---

5. Remove Items From Cart

Shows a frequency table of items currently in the cart.

Allows removing multiple quantities at once.

Restores stock back to the inventory.

Shows error if:

Item is not in cart

User tries to remove more than they have




---

6. Checkout System

During checkout, the program displays:

✔ Frequency Table (Billing Table)

Item name

Quantity

Unit price

Subtotal per item


✔ Total Calculation

Calculates total amount.

Option to apply coupon.



---

7. Coupon System

Supports SAVE10 coupon.

Gives 10% discount on the total bill.

Validates coupon code.



---

8. Receipt Generation

Generates a .txt receipt file.

Receipt contains:

Customer name

Order ID

All items with quantities and subtotals

Final payable amount

Delivery address

Estimated delivery date




---

9. Randomized Order & Delivery System

Generates a random 5-digit Order ID.

Delivery date calculated using:

Random number of days (3–7)

Current date




---

10. Cart & Inventory Reset

After checkout:

Cart is cleared

Stock is already updated


Prepares system for next customer session.



---

11. User-Friendly Menu

The main menu includes:

1. View Items


2. Add Item to Cart


3. Remove Item from Cart


4. Checkout


5. Exit




---

🎯 Purpose of the Project

This project is perfect for learning:

Python dictionaries

Lists

File handling (receipt generation)

Random numbers

Functions & loop control

Inventory management

Billing system logic

Basic user input validation


<img width="661" height="682" alt="Screenshot 2025-11-25 at 12 32 25 AM" src="https://github.com/user-attachments/assets/89ca0d5a-6f86-4c81-90b9-17239db5494e" />
<img width="644" height="667" alt="Screenshot 2025-11-25 at 12 33 10 AM" src="https://github.com/user-attachments/assets/a62ca3da-6597-492b-a7af-596162d5d3a8" />
<img width="644" height="672" alt="Screenshot 2025-11-25 at 12 33 43 AM" src="https://github.com/user-attachments/assets/9ef9c503-d27a-4522-91b6-ce4fe5d51a00" />
<img width="685" height="684" alt="Screenshot 2025-11-25 at 12 34 29 AM" src="https://github.com/user-attachments/assets/53bcc42a-7aae-4775-a948-f11a4e9702c3" />
<img width="363" height="101" alt="Screenshot 2025-11-25 at 12 34 43 AM" src="https://github.com/user-attachments/assets/9c97f573-017e-4fc6-a3d1-9e44b21e30d6" />



