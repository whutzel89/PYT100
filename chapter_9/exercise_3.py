class NotPerson:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class FamilyError(Exception):
    def __init__(self):
        self.message=" is not class Person"
        super().__init__(self.message)

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
        if not isinstance(mom,Person):
            raise FamilyError()
        elif not isinstance(dad,Person):
            raise FamilyError()
        self.myfamily = [mom,dad]
        for arg in args:
            if not isinstance(arg,Person):
                raise FamilyError()
            else:
                self.myfamily.append(arg)
        self.kids = len(self.myfamily)-2

    def add(self,kid):
        if not isinstance(kid,Person):
            raise FamilyError
        else:
            self.myfamily.append(kid)
            self.kids+=1

    def __eq__(self,other):
        if isinstance(other,Person):
            return self.kids == other.kids
        else:
            raise FamilyError()

    def __lt__(self,other):
        if isinstance(other,Person):
            return self.kids < other.kids
        else:
            raise FamilyError()

    def __gt__(self,other):
        if isinstance(other,Person):
            return self.kids > other.kids
        else:
            raise FamilyError()

    def __str__(self):
        return str(self.myfamily)
        

if __name__ == "__main__":
    mom = Person("cathy", 64, "F")
    dad = Person("gary", 66, "M")
    me = Person("will", 34, "M")
    bro = Person("andy", 30, "M")
    sis = Person("Fran", 28, "F")
    bob = NotPerson("smeegle",2453,"?")

    myfam = Family(mom,dad,me,bro)

    othfam = Family(mom,dad,bro)

    print(me)
    print(myfam)
    print(myfam>othfam)
    print(myfam<othfam)
    othfam.add(sis)
    print(myfam==othfam)
    print(myfam)
 
