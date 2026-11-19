n = int(input("Enter a positive integer: "))

print("\nNormal Pattern:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nInverted Pattern:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print(f"\nMultiplication Table (1 to {n}):")
for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 15)