import json
from Student import Student
s = Student(1000,"Atul",30)

#print(s.__dict__)
#json_string = json.dumps(s.__dict__)

with open("file-collection/student.json","w") as f:
    json.dump(s.__dict__,f)
    print("operation success...")