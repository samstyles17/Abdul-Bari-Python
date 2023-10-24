class Employee:
    ecount = 0
    
    def __init__(self,name,sal,des) -> None:
        Employee.ecount += 1
        self.name = name
        self.sal = sal
        self.eid = Employee.ecount
        self.des = des
        
    def empDetails(self):
        print('Employee Name:',self.name," Salary::",self.sal," EmpID:",self.eid," Designation:",self.des)
        
e = Employee('Harsh',20000,'Manager')
e.empDetails()