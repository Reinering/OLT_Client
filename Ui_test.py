

class A(object):

    def __init__(self):
        self.age = "17"
        print("创造A")
    def pringAge(self):
        print("Age of A:",self.age)

class C(A):
    def __init__(self, sex):
        super().__init__()
        self.sex = sex
        print("创造C")
    def printSex(self):
        print("Sex of C:", self.sex)

class AA(object):
    def __int__(self):
        self.name = "AA"
        print("创造AA")
    def pA(self):
        print("Name of AA:", self.name)


if __name__ == "__main__":
    A().pringAge()
    C("girl")
    aa = AA()
    aa.pA()