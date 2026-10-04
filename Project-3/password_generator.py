import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    all_characters = letters + numbers + special_characters

    for i in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    password = "".join(password)

    print("\nGenerated Password:", password)
    print("Password Length:", len(password))