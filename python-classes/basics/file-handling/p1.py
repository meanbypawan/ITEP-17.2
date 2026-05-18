from pathlib import Path
from datetime import datetime
import os
path = Path("file-collection/abc.txt")

print(f"Name : {path.name}")
print(f"Abosulte Path : {path.absolute()}")
print(f"isFile : {path.is_file()}")
print(f"isDirectory : {path.is_dir()}")
print(f"Size :  {path.stat().st_size} bytes")
mtime = path.stat().st_mtime
time = datetime.fromtimestamp(mtime)
print(f"Last Modifiled : {time.day}/{time.month}/{time.year} {time.hour} : {time.minute}")
print(f"isReadable : {os.access(path,os.R_OK)}")
print(f"isWritable : {os.access(path,os.W_OK)}")
print(f"isExecutable : {os.access(path,os.X_OK)}")