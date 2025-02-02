import argparse
import random
import string

def Generate_password(length, uppercase, lowercase, digits, special_chars):
    password = ''
    if length:
        password += string.ascii_uppercase
    if  uppercase:
        password += string.ascii_lowercase
    if digits:
        password+= string.digits
    if special_chars:
        password += string.punctuation
    if not password:
        raise ValueError("Atleast one charater ")
    password_Genarator = ''.join(random.choice(password) for _ in range(length))
    return password_Genarator

def main():
    parser = argparse.ArgumentParser(description='Random Password Generator')
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-lo', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')
    args = parser.parse_args()
    try:
        password_Genarator = Generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
        print(f"Generated Random password: {password_Genarator}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()
