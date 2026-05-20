import jsonpickle
'''
  Custom -object --> json string
  jsonpickle.encode(s)
  jsonpickle.decode()
'''
from Student import Student

s = Student(101,"XYZ",29)

def write_custom_object():
    json_string = jsonpickle.encode(s)
    try:
      with open("file-collection/student.json","a") as f:
        f.write(json_string)
        print("Operation success....")
    except Exception as e:
      print(e)

def read_custom_object():
   try:
      with open("file-collection/student.json","r") as f:
         json_data = f.read()
         s = jsonpickle.decode(json_data)
         print(s)
   except Exception as e:
      print(e)

read_custom_object()
