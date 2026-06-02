from mysql.connector import pooling
from dotenv import load_dotenv
import os
load_dotenv()
print(f"Database name  :{os.getenv('DB_NAME')}")
pool = pooling.MySQLConnectionPool(host=os.getenv("DB_HOST","localhost"),
                            user=os.getenv("DB_USER"),
                            password=os.getenv("DB_PASSWORD"),
                            database=os.getenv("DB_NAME"),
                            pool_size=10)

