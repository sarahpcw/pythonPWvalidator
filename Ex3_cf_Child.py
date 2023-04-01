from Ex3_cf_Parents import cfunctions   #from filename import classname

class cf(cfunctions): # classname   = inheritance  
    # cfunction  is the base class, superclass, parent class
    
    def __init__(self,name):
        super().__init__(name)
        self.name = name
        
    def printFinalMessage(self):
        print("thank you, the end, from ", self.name)
    
    def calcTravelFee(self, distance): ####### override
       fee =0
       if distance < 20 :
            fee = 0  
       elif distance >= 20 and distance< 40 :
            fee = 10
       elif distance >= 40 :
             fee = 20
       return fee

  
        