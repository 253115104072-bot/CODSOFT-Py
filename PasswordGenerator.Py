import random
import string

print("=" * 50)
print("         PASSWORD GENERATOR")
print("=" * 50)

while True:
    print("\nChoose Password Strength")
    print("1. Weak (Letters only)")
    print("2. Medium (Letters + Numbers)")
    print("3. Strong (Letters + Numbers + Symbols)")

    choice = input("Enter your choice (1/2/3): ")

    length = int(input("Enter the password length: "))

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if choice == "1":
        characters = letters
        strength = "Weak"

    elif choice == "2":
        characters = letters + numbers
        strength = "Medium"

    elif choice == "3":
        characters = letters + numbers + symbols
        strength = "Strong"

    else:
        print("Invalid Choice! Please try again.")
        continue

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n" + "=" * 50)
    print("Password Strength :", strength)
    print("Generated Password:", password)
    print("=" * 50)

    print("\nPassword Statistics")
    print("Length:", len(password))
    print("Contains Letters :", any(c.isalpha() for c in password))
    print("Contains Numbers :", any(c.isdigit() for c in password))
    print("Contains Symbols :", any(c in string.punctuation for c in password))

    again = input("\nDo you want to generate another password? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using the Password Generator!")
        print("Have a great day!")
        break
