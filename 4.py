correct_user = "admin"
correct_pass = "pass123"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "" or password == "":
        print("Username or password cannot be empty!")
        continue

    if username == correct_user and password == correct_pass:
        print("Login successful! Welcome.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect credentials. Attempts remaining: {attempts}")
        else:
            print("Account locked due to 3 failed attempts.")