import re
def valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(pattern,email) else False
emails=["vijay.kuamr@example.com",
        "arunaannam@gmail.com",
        "abhianav-email",
        "chandu.smith@gmail",
        "rohithbaddam",
        "priyak@123.45"
]
for i in emails:
    print(f'{i} is a valid email address' if valid_email(i) \
          else f'{i} not a valid email address')
