start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

prime_count = 0
prime_sum = 0

print("Prime numbers:", end=" ")
for num in range(start, end + 1):
    if num < 2:
        continue
        
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num, end=" ")
        prime_count += 1
        prime_sum += num

print(f"\nTotal primes found: {prime_count}")
print(f"Sum of primes: {prime_sum}")