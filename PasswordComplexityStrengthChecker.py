import re

def check_password_strength(password):
    feedback = []
    strength_points = 0

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Digit check
    if re.search(r'[0-9]', password):
        strength_points += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_points += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    # Final strength rating
    if strength_points == 5:
        strength = "Very Strong"
    elif strength_points == 4:
        strength = "Strong"
    elif strength_points == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
