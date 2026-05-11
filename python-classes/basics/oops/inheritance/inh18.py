from abc import *

class Shape(ABC):
  @abstractmethod
  def get_area(self):
    pass    

class Circle(Shape):
    def get_area(self):
       r =  float(input("Enter radius.."))
       print(f"Area of circel is :{3.14*r*r}")

class Traingle(Shape):
    def get_area(self):
        b = int(input("Enter base : "))
        h = int(input("Enter height : "))
        print(f"Traingle Area : {1/2 * b * h}")

class Rectangle(Shape):
    def get_area(self):
       l =  int(input("Enter length : "))        
       w = int(input("Enter width : "))
       print(f"Rectangel Area : {l*w}")


print("Press 1 for circle")
print("Press 2 for traingle")
print("Press 3 for rectange")

choice = int(input("Input your choice : "))
obj = None
if choice == 1:
   obj = Circle()
elif choice == 2:
    obj = Traingle()
elif choice == 3:
    obj = Rectangle()

obj.get_area()           