def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    print("==== Caesar Cipher Encryption/Decryption ====")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter E or D.")
        return

    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter the shift value (0-25): "))
        if not (0 <= shift <= 25):
            raise ValueError
    except ValueError:
        print("Invalid shift. Please enter an integer between 0 and 25.")
        return

    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
