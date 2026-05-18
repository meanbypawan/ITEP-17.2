'''
  transient :-
'''
class Customer:
    def __init__(self,id,name,contact,age):
        self.__id = id
        self.__name = name
        self.__contact = contact
        self.__age = age

    def __str__(self):
        return str(self.__id)+ " : "+self.__name + " : "+str(self.__contact)+" : "+str(self.__age)     
    
    # It will execute during serialization process :- dump
    def __getstate__(self):
        print("__getstate__ called....")
        return {
            "id": self.__id,
            "name": self.__name,
            "age":self.__age
        }