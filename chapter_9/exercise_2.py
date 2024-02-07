class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.name+" "+str(+self.age)+" "+self.gender
    def __repr__(self):
        return str(self)

class Family(Person):
    def __init__(self, mom,dad,*args):
        self.myfamily = [mom,dad]
        for arg in args:
            self.myfamily.append(arg)

    def add(self,kid):
        self.myfamily.append(kid)

    def __str__(self):
        return str(self.myfamily)
        

if __name__ == "__main__":
    mom = Person("cathy", 64, "F")
    dad = Person("gary", 66, "M")
    me = Person("will", 34, "M")
    bro = Person("andy", 30, "M")
    sis = Person("Fran", 28, "F")

    myfam = Family(mom,dad,me,bro)

    print(me)
    print(myfam)
    myfam.add(sis)
    print(myfam)
