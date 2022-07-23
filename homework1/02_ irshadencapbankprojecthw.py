class Bank(object):
    def __init__(self,accounttype,username,accountnumber,amount,withdraw):
        self.accounttype=accounttype
        self.username=username
        self.__accountnumber=accountnumber
        self.amount=amount
        self.withdraw=withdraw
        
    def balance(self):
        return self.amount-self.withdraw
    
    def get_accountnumber(self):
        return self.__accountnumber
    
    
    def set_accountnumber(self,pp):
        self.__accountnumber=pp
        
        
    
        
    
    def __repr__(self):
        return f'object("{self.accounttype},{self.username},{self.amount},{self.withdraw}")'
    
    
    
if __name__=="__main__":
        CIBC=Bank("Chechking","Hashir",154567,100000,2000)
        print(CIBC)
        CIBC.set_accountnumber(143256)
        print(CIBC.__repr__())
        print(CIBC.balance())
        print(CIBC.get_accountnumber)
        print(CIBC.get_accountnumber())
        
        
        
  



        
        
        
        
        
        