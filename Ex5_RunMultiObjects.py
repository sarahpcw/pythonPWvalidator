#######################
## 
######################

from Ex4_Child import cf   # from filename import classname , specifies where code is to be found

obj = cf("ABC Carpetshop",1.2)        
obj.printCompanyMessage()
obj.printPersonalGreeting()
w,l = obj.carpetlengthWidth()
area = obj.calcArea(l,w)    
print ( "Area", area )
cp = obj.calcPrice(area)  ## which version of calcprice is used : the one in the child (override)
print ( "the carpetprice  ", (cp))
cp = obj.calcVat(cp)
print ( "the carpetprice + vat ", (cp))
obj.printFinalMessage()


obj1 = cf("Express carpets",1.175)        
obj1.printCompanyMessage()
obj1.printPersonalGreeting()
w,l = obj1.carpetlengthWidth()
area = obj1.calcArea(l,w)    
print ( "Area", area )
cp = obj1.calcPrice(area)  ## which version of calcprice is used : the one in the child (override)
print ( "the carpetprice  ", (cp))
cp = obj1.calcVat(cp)
print ( "the carpetprice + vat ", (cp))
obj1.printFinalMessage()