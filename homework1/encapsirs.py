#public scope of variables and methdos
class Demo1(object):

    def __init__(self,x,y):
        self.x=x# default all variable and methods are public 
        self.y=y

    def product(self):
        return self.x*self.y

    def sum(self):
        return self.x+self.y


#protected scope 
class House(object):
    def __init__(self, accessCodePassword, ownership,address):
        #private instance variable
        self.__accesspwd=accessCodePassword #private scope
        #protected instance variable
        self._ownership=ownership #protected scope

    #getter method
    def getPassword(self):
        return self.__accesspwd

    #setter method 
    def setNewPassword(self,newPass):
        self.__accesspwd=newPass
  

if __name__=="__main__":
    val=Demo1(10,20)
    print(val.product())
    print(val.sum())
    whitehouse=House("7240","BarakObama","Washington")
    # print(whitehouse.__accesspwd)
    print(whitehouse.getPassword())
    print(whitehouse._ownership)

