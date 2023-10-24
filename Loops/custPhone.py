class Phone:
    def __init__(self,name,phno) -> None:
        self.name = name
        self.phno = phno
        
    def getName(self):
        return self.name
    
    def getPhno(self):
        return self.phno

    def setPhno(self,p):
        self.phno = p
        

c1 = Phone('Harsh',9523835835)
print(c1.getName())
print(c1.getPhno())

c1.setPhno(9386348962)
print(c1.getPhno())