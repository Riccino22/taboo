import random
import string

def generate(length=10):
    characters = string.ascii_letters + string.digits
    result = ''.join(random.choice(characters) for _ in range(length))
    return result


