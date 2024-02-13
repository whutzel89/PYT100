class Employee:
    def __init__(self,name,salary,years):
        self.name = name
        self.salary = salary
        self.years = years

    def pension(self):
        return self.years*self.salary*.1

    def getname(self):
        return self.name


class Manager(Employee):
    def pension(self):
        return self.years*self.salary*.2

class Executive(Manager):
    def pension(self):
        return self.years*self.salary*.3

if __name__ == "__main__":
    emp = Employee('bob',10000,10)
    man = Manager('jim',10000,10)
    execu = Executive('rick',10000,10)
    print(emp.getname())
    print(emp.pension())
    print(man.getname())
    print(man.pension())
    print(execu.getname())
    print(execu.pension())
