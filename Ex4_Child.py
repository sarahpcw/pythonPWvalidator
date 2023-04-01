from Ex4_Parents import cfunctions   #from filename import classname

class cf(cfunctions): # classname   = inheritance  
    # cfunction  is the base class, superclass, parent class
    
    def __init__(self,name, vat):
        super().__init__(name)
        self.name = name
        self.vat = vat
        
    def printFinalMessage(self):
        print("thank you, the end, from ", self.name," Child class! \n")
    
    def calcVat (self, cp):
         cp = cp*self.vat
         return cp
  
        