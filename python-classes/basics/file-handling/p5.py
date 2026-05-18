'''
  r :-  Open the file in read mode , if file not available then raise FileNotFoundError.
        It is default mode
  w :- Open the file in write mode. if file exist then erase all the data. 
       if not exist then it will create new file      
  a :- open the file in append mode. if file exist then append the data at the end.
  if not exist then it will create new file
  
  r+[Read-Write Mode] :- open the file in read and write mode. if file not exist then raise FileNotFoundError
     if file exist and you perform write operation then data will be replaced character by chracter from the begining
     because default cursor position is 0
  
  w+[Write-Read Mode]:- Open the file in Write-Read mode. if file exist then it will erase all the data and write new data.
  if file not exist then it will create new file. 
  
  a+ [Append-Read] :- Open the file in Append-Read operations. if file not exist then it will create new file.
  if file exist then it will append data into file at the last because
  default cursor position is EOF
  '''
f = None
try:
    f = open("file-collection/xy.txt","a+")
    print(f"Default Cursor Position : {f.tell()}")
    f.write("\nThis is second test data")
    f.seek(0)
    data = f.read()
    print(f"Read Operation : {data}")
except OSError as e:
    print(e)
finally:
    if f is not None:
        f.close()    