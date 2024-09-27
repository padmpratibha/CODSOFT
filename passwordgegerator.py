import random
import string


def generate_password(length = 12):

    letters = string.ascii_letters
    digits = string.digits
    panctuation = string.punctuation


    all_char = letters + digits + panctuation
    password = ''.join(random.choice(all_char) for i in range(length))
    return password


password = generate_password(12)
print(f"Your Password is :{password}")
