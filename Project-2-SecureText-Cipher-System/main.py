def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            result += char

    return result


while True:

    
    print("      BASIC ENCRYPTION & DECRYPTION TOOL")
    

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nSelect an option (1-3): ")

    if choice == "1":

        text = input("\nEnter Message: ")
        shift = int(input("Enter Shift Key: "))

        encrypted_text = encrypt(text, shift)

        print("\n----- RESULT -----")
        print("Original Message :", text)
        print("Encrypted Message:", encrypted_text)

    elif choice == "2":

        text = input("\nEnter Encrypted Message: ")
        shift = int(input("Enter Shift Key: "))

        decrypted_text = decrypt(text, shift)

        print("\n----- RESULT -----")
        print("Encrypted Message:", text)
        print("Decrypted Message:", decrypted_text)

    elif choice == "3":

        print("\nThank you for using the Encryption Tool.")
        break

    else:

        print("\nInvalid Option! Please select 1, 2, or 3.")