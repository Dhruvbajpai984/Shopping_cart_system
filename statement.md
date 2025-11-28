#  Problem Statement

The goal of this project is to create a **simple, efficient, and user-friendly Shopping Cart Billing System** that works entirely in the terminal.  
Users should be able to browse available products, add items to their cart, review their selections, and generate a final bill during checkout.

The system must:
- Provide a clean and readable code structure  
- Handle flexible product name inputs (e.g., `rice`, `Rice`, `RICE`, `rice1kg`)  
- Maintain product stock  
- Automatically calculate totals  
- Be easy to run without any external dependencies  


# Scope of the Project

This project focuses on building a **console-based billing software** with the following scope:

### Included in Scope
- Display available products  
- Search and match product names intelligently  
- Add items to cart  
- Update & manage stock  
- View cart summary  
- Generate a bill at checkout  
- Clear cart after checkout  
- Work on any system running Python  
- Beginner-friendly, readable source code  

### Not Included in Scope
- GUI/desktop interface  
- Online payment system  
- Database storage (uses in-memory dictionaries only)  
- Mobile or web application version  


# Target Users

This project is designed for:

- **Beginner Python learners** practicing loops, lists, dictionaries & functions  
- **Students** required to submit a Python mini-project  
- **Small businesses or shops** needing a simple offline billing tool  
- **Anyone wanting a simple CLI-based shopping cart system**  
- **Developers** looking for a base project to expand into GUI/web apps  


# High-Level Features

### Smart Product Search
- Automatically matches input like:
  - `rice`, `Rice`, `RICE`, `rice1kg`, `ri ce`, etc.
- Uses normalization + substring matching

### Cart Management
- Add multiple items  
- Updates stock in real-time  
- Stores items and their quantities  

### Billing & Checkout
- Displays itemized bill  
- Calculates total automatically  
- Clears cart after checkout  

### Product Inventory
- Displays all products with:
  - Name  
  - Price  
  - Stock availability  

### Clean Code
- No external libraries  
- Fully readable and maintainable  
- Safe input handling  

