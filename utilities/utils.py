import random
import string

class Utils:
    @staticmethod
    def generate_random_email():
        username_chars = string.ascii_letters + string.digits + '._%+-'
        domain_chars = string.ascii_letters + string.digits + '-'

        username_length = random.randint(5, 15)  # Random length between 5 and 15
        username = ''.join(random.choice(username_chars) for _ in range(username_length))

        domain_length = random.randint(3, 10)  # Random length between 3 and 10
        domain = ''.join(random.choice(domain_chars) for _ in range(domain_length))

        tlds = ['com', 'net', 'org', 'edu', 'gov', 'mil', 'int']
        tld = random.choice(tlds)

        email = f"{username}@{domain}.{tld}"
        return email