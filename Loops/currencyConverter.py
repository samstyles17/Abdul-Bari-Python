class Currency:
    def __init__(self,cur,rate) -> None:
        self.curr = cur
        self.rate = rate
        
    def getCurr(self):
        return self.curr
    
    def setCurr(self,c):
        self.curr = c
        
    def getRate(self):
        return self.rate
    
    def setRate(self,r):
        self.rate = r
        
    def currConvert(self,amt) -> float:
        return amt*self.rate
    
c1= Currency('USD',80)
c1.getCurr()
c1.setCurr('USD')
c1.getRate()
c1.setRate(60)
print(c1.currConvert(100))