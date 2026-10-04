# Python Random Password Generator

This is my third project for the DecodeLabs Python Programming internship.

## About the Project

I created a Random Password Generator using Python. The program asks the user for the required password length and generates a random password containing letters, numbers, and special characters.

This project helped me understand how Python modules can be used to create a simple and useful security-related application.

## Features

- Accepts password length from the user
- Generates a random password
- Includes letters, numbers, and special characters
- Ensures the password has the requested length
- Displays the generated password
- Displays the password length
- Checks that the minimum password length is 4

## Python Concepts Used

- `import`
- `random` module
- `string` module
- `random.choice()`
- `random.shuffle()`
- Lists
- `for` loop
- `if-else`
- String manipulation
- User input

## How It Works

1. The user enters the required password length.
2. The program checks whether the length is at least 4.
3. A letter, number, and special character are selected.
4. Additional characters are randomly selected until the required length is reached.
5. The characters are shuffled.
6. The generated password is displayed.

## Example

```text
===== RANDOM PASSWORD GENERATOR =====
Enter password length: 8

Generated Password: MP9k;|GE
Password Length: 8
