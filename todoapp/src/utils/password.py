import bcrypt

def hash_password(password:str):
    password_bytes = password.encode('utf-8')
    salt_key = bcrypt.gensalt(12)
    return bcrypt.hashpw(password_bytes, salt_key).decode('utf-8')

def verify_password(password:str,hash_password):
    password_bytes = password.encode('utf-8')
    hash_password_bytes = hash_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_password_bytes)