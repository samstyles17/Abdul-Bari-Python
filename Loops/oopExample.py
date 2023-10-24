class SampleClass:
    count = 0
    def __init__(self,length,breadth) -> None:
        self.length = length
        self.breadth = breadth
        SampleClass.count += 1
        
    def area(self) -> int:
        return self.length * self.breadth
   
    def incCount(self) -> int:
        return SampleClass.count    
    
c1  = SampleClass(10,10)
c2 = SampleClass(11,11)
print(c2.incCount())
    
    
    