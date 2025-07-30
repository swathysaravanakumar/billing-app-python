print("🛒 Welcome to Swathy's Billing System 🛒\n")

items = []

while True:
    name = input("Enter item name: ")
    price = float(input("Enter item price: ₹"))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
    items.append([name, price, quantity, total])
    
    more = input("Add another item? (y/n): ")
    if more.lower() != 'y':
        break

print("\n🧾 Final Bill 🧾")
print("-" * 40)
print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Price", "Qty", "Total"))
print("-" * 40)

grand_total = 0

for item in items:
    print("{:<15} ₹{:<9.2f} {:<10} ₹{:<9.2f}".format(item[0], item[1], item[2], item[3]))
    grand_total += item[3]

print("-" * 40)
print(f"Grand Total: ₹{grand_total:.2f}")
print("-" * 40)
print("Thank you for shopping! 💐")
