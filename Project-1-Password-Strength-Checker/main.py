def evaluate_password(password):

    score = 0

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False

    special_characters = "!@#$%^&*()-_=+[]{}|\\:;'<>,.?/"

    # Length Check
    if len(password) >= 8:
        score += 1

    # Character Analysis
    for char in password:

        if char.isupper():
            has_uppercase = True

        elif char.islower():
            has_lowercase = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special_char = True

    # Update Score
    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_digit:
        score += 1

    if has_special_char:
        score += 1

    # Determine Strength
    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"

    return (
        strength,
        has_uppercase,
        has_lowercase,
        has_digit,
        has_special_char
    )


# Main Program

password = input("Enter Password: ")

strength, upper, lower, digit, special = evaluate_password(password)

print("\nPassword Analysis")
print("---------------------")
print("Contains Uppercase Letters :", upper)
print("Contains Lowercase Letters :", lower)
print("Contains Numbers           :", digit)
print("Contains Special Characters:", special)

print("\nPassword Strength :", strength)
