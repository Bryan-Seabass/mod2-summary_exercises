items = []
quantities = []
prices = []

for x in range(3):
    items.append(input("Enter the item: "))
    quantities.append(float(input("Enter the quantity: ")))
    prices.append(float(input("Enter the price: ")))

total = sum(quantities[x] * prices[x] for x in range(3))

print("\nYou are purchasing:")
for x in range(3):
    print(f"{quantities[x]}x {items[x]}")

print(f"\n Total Cost: {total}")