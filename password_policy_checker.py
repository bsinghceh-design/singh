# password_policy_checker.py

import string

def check_password_policy(password):
    """
    Simple rule-based checker:
    - At least 8 characters
    - At least 1 uppercase
    - At least 1 lowercase
    - At least 1 digit
    - At least 1 special character
    Returns: dict with 'status' and 'reasons' list.
    """
    reasons = []
    status = "Strong"

    if len(password) < 8:
        status = "Weak"
        reasons.append("Password must be at least 8 characters long.")

    if not any(c.isupper() for c in password):
        status = "Weak"
        reasons.append("Password must contain at least one uppercase letter.")

    if not any(c.islower() for c in password):
        status = "Weak"
        reasons.append("Password must contain at least one lowercase letter.")

    if not any(c.isdigit() for c in password):
        status = "Weak"
        reasons.append("Password must contain at least one digit.")

    special_chars = string.punctuation
    if not any(c in special_chars for c in password):
        status = "Weak"
        reasons.append("Password must contain at least one special character (e.g. @, #, !).")

    # If all basic rules passed but length < 12, mark as Medium
    if status == "Strong" and len(password) < 12:
        status = "Medium"
        reasons.append("Consider using 12+ characters for stronger security.")

    return {
        "password": password,
        "status": status,
        "reasons": reasons
    }


if __name__ == "__main__":
    demo = "Pass123"
    print(check_password_policy(demo))
