item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
subtotal = item_price * quantity
tax = (subtotal * 13)/100
total = subtotal + tax
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
