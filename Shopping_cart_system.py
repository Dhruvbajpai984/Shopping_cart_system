products = {
    "Rice 1kg": [60, 20], "Wheat Flour 1kg": [45, 18], "Sugar 1kg": [50, 25],
    "Milk 1L": [55, 22], "Eggs 6pc": [40, 30], "Bread": [30, 15],
    "Butter 200g": [48, 10], "Cheese 200g": [75, 9], "Tea 250g": [110, 10],
    "Coffee 200g": [150, 8], "Salt 1kg": [20, 40], "Oil 1L": [135, 17],
    "Soap": [35, 25], "Shampoo 200ml": [95, 12], "Toothpaste": [60, 20],
    "Pen": [10, 50], "Notebook": [40, 28], "Pencil": [5, 60],
    "Eraser": [3, 40], "Sharpener": [7, 35], "Water Bottle": [90, 10],
    "Chips": [20, 30], "Chocolate": [25, 25], "Biscuits": [15, 40],
    "Noodles": [12, 33], "Ketchup": [85, 12], "Jam": [75, 10],
    "Maggie Pack": [14, 36], "Detergent 1kg": [95, 14], "Tissue Pack": [35, 20]
}

cart_items = []
cart_prices = []

def normalize(text):
    return "".join(ch.lower() for ch in text if ch.isalnum())

def find_product(name):
    key = normalize(name)
    best_match = None

    for item in products:
        item_key = normalize(item)

        if item_key == key:
            return item

        if key in item_key:
            best_match = item

    return best_match


def show_products():
    print("\nAvailable Products:")
    for name, (price, qty) in products.items():
        print(f"{name} - ₹{price} ({qty} in stock)")
    print()

def add_to_cart():
    show_products()
    item_name = input("Enter product name: ")

    product = find_product(item_name)
    if not product:
        print("Item not found!\n")
        return

    qty = int(input("Quantity: "))
    price, stock = products[product]

    if qty > stock:
        print("Not enough stock!\n")
        return

    products[product][1] -= qty

    for _ in range(qty):
        cart_items.append(product)
        cart_prices.append(price)

    print(f"Added {qty} × {product}\n")

def view_cart():
    if not cart_items:
        print("Cart is empty!\n")
        return

    print("\nYour Cart:")
    total = 0
    counted = {}

    for item in cart_items:
        counted[item] = counted.get(item, 0) + 1

    for item, qty in counted.items():
        price = products[item][0]
        print(f"{item} × {qty} = ₹{price * qty}")
        total += price * qty

    print(f"Total: ₹{total}\n")

def checkout():
    if not cart_items:
        print("Cart is empty! Cannot checkout.\n")
        return

    print("\nCHECKOUT BILL:")
    total = 0
    counted = {}

    for item in cart_items:
        counted[item] = counted.get(item, 0) + 1

    for item, qty in counted.items():
        price = products[item][0]
        print(f"{item} × {qty} = ₹{price * qty}")
        total += price * qty

    print("")
    print(f"Grand Total: ₹{total}")
    print("Thank you for shopping!\n")

    cart_items.clear()
    cart_prices.clear()

def main():
    while True:
        print("1. Add to Cart")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_to_cart()
        elif choice == '2':
            view_cart()
        elif choice == '3':
            checkout()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
