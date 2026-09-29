import secrets
import string

def generate_divyanshi_password(total_length=18):
    base_name = "divyanshi"
    required_length = len(base_name) + 3 

    extra_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    full_pool = string.ascii_letters + string.digits + string.punctuation

    remaining_slots = total_length - len(base_name) - len(extra_chars)
    extra_chars.extend(
        secrets.choice(full_pool) for _ in range(remaining_slots)
    )

    secrets.SystemRandom().shuffle(extra_chars)

    password = base_name + "".join(extra_chars)
    return password

final_password = generate_divyanshi_password(total_length=18)
print(final_password)