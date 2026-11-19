terms = int(input("How many terms to generate? "))

if terms < 1:
    print("Please enter a number greater than 0.")
else:
    a, b = 0, 1
    total_sum = 0
    even_count = 0
    odd_count = 0

    for _ in range(terms):
        print(a, end=" ")
        total_sum += a
        
        if a % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
        a, b = b, a + b

    print(f"\nSum: {total_sum}")
    print(f"Even terms: {even_count}")
    print(f"Odd terms: {odd_count}")