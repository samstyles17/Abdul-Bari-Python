class Cuboid:
    def __init__(self,l=1,b=1,h=1):
        print(id(self))
        self.length  = l
        self.breadth = b
        self.height = h
        
    # def __init__():
    #     pass
    
    def lidArea(self):
        return self.length*self.breadth
    
    def volume(self):
        return self.length*self.breadth*self.height
 
 
c1 = Cuboid()
print("c1 volume = ",c1.volume())
c2 = Cuboid(12)
print("c2 volume = ",c2.volume())
c3 = Cuboid(10,12)
print('c3 volume',c3.volume())
c4 = Cuboid(10,5,4)
print(c4.volume())   

# c1 = Cuboid(10,5,3)
# print(id(c1))
# print(c1.volume())

# c2 = Cuboid(12,10,10)
# print(id(c2))
# print(c2.volume())
