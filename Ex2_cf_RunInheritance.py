# from filename import classname , specifies where code is to be found
from Ex2_cf_Lib_Child import cf

obj = cf( )    # create a memory resident copy of the class and all its functions
                    # create an object of class cf
                    # create an instance of class cf
                    # instantiate class cf
                    
                    
########## main flow of the program, here I call or execute the functions
# # prefix all function names with the object name

obj.printCompanyMessage() ## in parent100

obj.printPersonalGreeting('Peter') ## in parent

w,l = obj.carpetlengthWidth() ## in parent
 
area = obj.calcArea(l,w) ## in parent

print ( "Area", area )

if area > 1000 :
    print ( "Too big for us, sorry!")
elif area < 5:
    print ( "Too small for us, sorry!")
else:
    cp = obj.calcCarpetPrice(area)   ## in parent
    print ("Carpet price :" , cp)

obj.printFinalMessage()

 