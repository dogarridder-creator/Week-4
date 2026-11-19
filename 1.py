passed = 0
failed = 0
total_marks = 0
highest_mark = -1
count = 0

while count < 10:
    mark = float(input(f"Enter marks for student {count + 1} (0-100): "))
    
    if mark < 0 or mark > 100:
        print("Invalid mark! Please enter a value between 0 and 100.")
        continue

    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")

    if mark >= 50:
        passed += 1
    else:
        failed += 1

    if mark > highest_mark:
        highest_mark = mark
    total_marks += mark
    count += 1

average = total_marks / 10
print(f"\nPassed: {passed}, Failed: {failed}")
print(f"Highest Mark: {highest_mark}")
print(f"Class Average: {average:.2f}")