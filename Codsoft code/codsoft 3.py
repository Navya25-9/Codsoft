import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    try:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
