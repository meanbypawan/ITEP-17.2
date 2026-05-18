print("At the start....")
f = None
try:
    f = open("file-collection/abc.txt","r")
    print(f"Current Position : {f.tell()}")
    f.read(1)
    print(f"Current Position : {f.tell()}")
    f.read(10)
    print(f"current postion : {f.tell()}")
    f.seek(3)
    print(f"After Seek curson position : {f.tell()}")
except OSError as e:
    print(e)
finally:
    if f is not None:
        f.close()   

print("At the end...")        