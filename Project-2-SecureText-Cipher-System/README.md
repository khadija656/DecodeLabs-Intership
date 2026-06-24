 SecureText Cipher System

A Python-based Encryption and Decryption tool that implements the Caesar Cipher algorithm to secure text messages. This project demonstrates the fundamental concepts of cryptography, data confidentiality, and secure communication through a simple yet effective substitution cipher technique.

---

##  Project Overview

The SecureText Cipher System is designed to encrypt and decrypt user messages using a user-defined shift key. The project helps in understanding how classical cryptographic techniques work and how encrypted data can be restored back to its original form through the decryption process.

This project was developed as part of a Cyber Security Internship to strengthen practical knowledge of encryption concepts and secure data handling.

---

##  Objectives

- Understand the basics of cryptography.
- Implement the Caesar Cipher algorithm.
- Perform text encryption using a shift key.
- Restore encrypted text through decryption.
- Learn the use of ASCII values with `ord()` and `chr()`.
- Build a menu-driven Python application.
- Explore data confidentiality concepts.

---

##  Features

✔ Encrypt user messages

✔ Decrypt encrypted messages

✔ User-defined shift key

✔ Supports uppercase and lowercase letters

✔ Preserves spaces and special characters

✔ Interactive menu-driven interface

✔ Input → Process → Output (IPO) implementation

✔ Encryption and decryption validation

✔ Simple and user-friendly console interface

---

## Technologies Used

- Python 3
- VS Code
- Git & GitHub

---

##  Working Principle

The project uses the Caesar Cipher encryption technique.

### Encryption Process

Each alphabet character is shifted forward by a specific number of positions based on the user-provided key.

Example:

```text
Original Text : HELLO
Shift Key     : 3

Encrypted Text: KHOOR
```

### Decryption Process

The encrypted text is shifted backward by the same key value to recover the original message.

```text
Encrypted Text: KHOOR
Shift Key     : 3

Decrypted Text: HELLO
```

---

## Mathematical Logic Used

The project utilizes:

- `ord()` → Converts characters into ASCII values.
- `chr()` → Converts ASCII values back into characters.
- `% 26` → Handles alphabet wrapping.

Example:

```python
(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
```

This ensures that:

```text
Z + 3 = C
```

instead of generating invalid characters.

---

## Project Structure


SecureText-Cipher-System/
│
├── main.py
├── README.md
└── screenshots/
```

---

```

### Run Program

```bash
python main.py
```

---

##  Sample Output

```text
==================================================
      BASIC ENCRYPTION & DECRYPTION TOOL
==================================================

1. Encrypt Message
2. Decrypt Message
3. Exit

Select an option (1-3): 1

Enter Message: Cyber Security
Enter Shift Key: 3

----- RESULT -----

Original Message : Cyber Security
Encrypted Message: Fbehu Vhfxulwb
```

### Decryption Example

```text
Select an option (1-3): 2

Enter Encrypted Message: Fbehu Vhfxulwb
Enter Shift Key: 3

----- RESULT -----

Encrypted Message: Fbehu Vhfxulwb
Decrypted Message: Cyber Security
```

---

##  Cyber Security Concepts Covered

- Data Confidentiality
- Encryption
- Decryption
- Cryptography Fundamentals
- Secure Communication
- Character Encoding
- Data Protection Basics

---

##  Future Enhancements

- Graphical User Interface (GUI)
- File Encryption Support
- Multiple Encryption Algorithms
- Vigenère Cipher Implementation
- Password-Protected Encryption
- Advanced Cryptographic Techniques

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Python Programming
- Cryptographic Logic Building
- Caesar Cipher Implementation
- ASCII Character Manipulation
- Problem Solving
- Secure Data Handling

---

##  Author

**Khadija**

Cyber Security Intern | DecodeLabs

Passionate about Cyber Security, Cryptography, Ethical Hacking, and Secure Software Development.

---

## Acknowledgement

This project was developed as part of the DecodeLabs Cyber Security Internship Program to enhance practical understanding of encryption and decryption mechanisms in modern cybersecurity.
