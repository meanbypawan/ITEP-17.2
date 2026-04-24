employee_list = [
  { "id": 1, "name": "Amit Sharma", "salary": 50000, "age": 28 },
  { "id": 2, "name": "Priya Verma", "salary": 62000, "age": 32 },
  { "id": 3, "name": "Rahul Singh", "salary": 45000, "age": 26 },
  { "id": 4, "name": "Neha Gupta", "salary": 70000, "age": 35 },
  { "id": 5, "name": "Vikas Yadav", "salary": 52000, "age": 30 },
  { "id": 6, "name": "Sneha Kapoor", "salary": 68000, "age": 34 },
  { "id": 7, "name": "Arjun Mehta", "salary": 48000, "age": 27 },
  { "id": 8, "name": "Pooja Nair", "salary": 75000, "age": 36 },
  { "id": 9, "name": "Karan Patel", "salary": 54000, "age": 29 },
  { "id": 10, "name": "Anjali Desai", "salary": 60000, "age": 31 }
]
# for i in range(len(employee_list)):
for emp in employee_list:
   print(f"Id : {emp["id"]}, Name : {emp["name"]}, Salary : {emp["salary"]}, Age : {emp["age"]}")    
