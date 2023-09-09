import re
def task3(password):
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    if len(password) < min_length:
        return "Weak:- Password should have at least 8 characters."
    elif not has_uppercase:
        return "Weak:- Password should contain at least one uppercase letter."
    elif not has_lowercase:
        return "Weak:- Password should contain at least one lowercase letter."
    elif not has_digit:
        return "Weak:- Password should contain at least one digit."
    elif not has_special:
        return "Weak:- Password should contain at least one special character."
    else:
        return "Strong - Password is sufficiently strong."

password = input("Enter a password : ")
result = task3(password)
print(result)
