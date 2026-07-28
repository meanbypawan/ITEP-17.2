import bcrypt


def hash_password(password:str):
    password_byte = password.encode("utf-8")
    salt_key = bcrypt.gensalt(12)
    return bcrypt.hashpw(password_byte, salt_key).decode("utf-8")

def verify_password(password:str, hash_password:str):
    password_byte = password.encode("utf-8")
    hash_password_byte = hash_password.encode("utf-8")
    return bcrypt.checkpw(password_byte, hash_password_byte)