
class employee(object):
    def __init__(self,empid,salary,desig):
        self.empid=empid
        self.__salary=salary    #private instances
        self.design=desig
        
   # getter method
   
    def get_salary(self):
        return self.__salary
    
    # setter method
    def set_salary(self,currentsalary):
        self.__salary=currentsalary  
        
    def __repr__(self): 
        return f'object("{self.empid},{self.design}")'        
                     
        
if __name__=="__main__":
    emp1=employee(546,100000,"proceesEngineer")
    emp2=employee(349,70,"businessAnalyst")
    print(emp1)
    print(emp2)
    print(emp1.__repr__())
    print(emp2.__repr__())
    emp1.set_salary(120000)
    emp2.set_salary(80000)
    print(emp1.get_salary)
    print(emp2.get_salary)
    print(emp1.get_salary())
    print(emp2.get_salary())   
        