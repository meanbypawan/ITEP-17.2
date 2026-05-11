#Employee, Developer, Manager
# super
class Employee:
    def work(self):
        print("Work in company....")

class Developer:
    def write_code(self):
        print("Writing code...")

class Manager(Employee,Developer):
    def manage_team(self):
        print("Manage team...")

obj = Manager()
obj.work()
obj.write_code()
obj.manage_team()        