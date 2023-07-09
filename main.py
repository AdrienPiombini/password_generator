import random
import string


def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password


length = int(input("Enter the length of password : "))
has_number = input("Do you want to have number (y/n) ? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n) ? ").lower() == "y"
password = generate_password(length, has_number, has_special)
print("Generate password is : ", password)
