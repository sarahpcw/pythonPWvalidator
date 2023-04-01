#######################
## INHERITANCE!!! Travel fee
######################

from Ex3_cf_Child import cf   # from filename import classname , specifies where code is to be found

obj = cf("ABC Carpetshop")        # create a memory resident copy of the class and all its functions
                    # create an object of class cf
                    # create an instance of class cf
                    # instantiate class cf
########## main flow of the program, here I call or execute the functions
# prefix all function names with the object name

obj.printCompanyMessage()

w,l = obj.carpetlengthWidth()
#
area = w * l       # + - * / ()
print ( "Area", area )
#
if area > 1000 :
    print ( "Too big for us, sorry!")
elif area < 5:
    print ( "Too small for us, sorry!")
else:
    cp = obj.calcPrice(area)  ## which version of calcprice is used : the one in the child (override)
    tf = obj.calcTravelFee(25) 
    print ( "the carpetprice + vat ", (cp+tf))
    
    
obj.printFinalMessage()
