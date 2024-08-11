import re

def check_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Initialize strength level
    strength_level = 0

    # Evaluate each criterion
    if length_criteria:
        strength_level += 1
    if lowercase_criteria:
        strength_level += 1
    if uppercase_criteria:
        strength_level += 1
    if digit_criteria:
        strength_level += 1
    if special_char_criteria:
        strength_level += 1

    # Provide feedback based on strength level
    if strength_level == 5:
        return "Strong Password", "Your password is strong!"
    elif strength_level >= 3:
        return "Moderate Password", "Your password is moderate. Consider adding more complexity."
    else:
        return "Weak Password", "Your password is weak. Consider making it longer and adding a mix of characters."

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()
