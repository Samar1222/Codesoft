import random


def generate_password(length=12):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits

    # Ensure minimum length is 8
    length = max(length, 8)

    # Generate random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


def main():
    while True:
        password_length = int(input("Enter the desired password length: "))
        generated_password = generate_password(password_length)
        print("_____________________________________________")
        print(f"Generated Password: {generated_password}")
        print("_____________________________________________")
        print("")
        
        user_choice = input("Do you want to generate another password? (yes/no): ").lower()
        if user_choice != 'yes':
            break


if __name__ == "__main__":
    main()