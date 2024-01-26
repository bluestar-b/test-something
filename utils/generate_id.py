
import hashlib
import time
import secrets
import string

def generate_unique_id():
    timestamp = str(int(time.time() * 1000))
    random_part = ''.join(secrets.choice(string.ascii_letters) for _ in range(6))
    data = timestamp + random_part
    truncated_hash = hashlib.sha256(data.encode()).hexdigest()[:12]
    return ''.join(secrets.choice((char.upper(), char.lower())) for char in truncated_hash)


