stock = 100
total_sold = 0

while stock > 0:
    sold = int(input(f"\nAvailable stock: {stock}. Enter quantity sold (-1 to stop): "))
    
    if sold == -1:
        break
    if sold <= 0:
        print("Error: Quantity must be greater than zero.")
        continue
    if sold > stock:
        print("Transaction rejected: Not enough stock available.")
        continue
        
    stock -= sold
    total_sold += sold

print(f"\nTotal units sold: {total_sold}")
print(f"Remaining stock: {stock}")