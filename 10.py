even_count = 0
odd_count = 0
largest = None
total_sum = 0
pos_count = 0

while True:
    num = int(input("Enter an integer (0 to stop): "))
    
    if num == 0:
        break
    if num < 0:
        continue
        
    pos_count += 1
    total_sum += num
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    if largest is None or num > largest:
        largest = num

if pos_count == 0:
    print("No positive numbers were entered.")
else:
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Largest positive number: {largest}")
    print(f"Sum: {total_sum}")
    print(f"Average: {total_sum / pos_count:.2f}")