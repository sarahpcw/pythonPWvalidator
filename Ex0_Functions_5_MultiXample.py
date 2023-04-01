#########
def carpetlengthWidth (  sqm_price):             # input parameter
    wi = input ( "What is the width ")       # w and l are local variables
    wi = float(wi)
    l = float ( input ("Enter the length of your carpet ") ) 
    print ("length ", l, "width" , wi , sqm_price)  
    return wi, l  # two return values

def calcprice ( area, sqm_price ):               # input parameter but no return value
    
    carpetprice = float( area ) * sqm_price  
    print ( "Carpet price", "$%.2f" % carpetprice)
    return carpetprice

def calcdiscount (  area, sqm_price ):               # input parameter but no return value
   if area > 500:
        discount = sqm_price * 0.1
   return discount

###########

w,l=carpetlengthWidth(10)
#
area = w * l       # + - * / ()
print ( "Area", area )
#
if area > 1000 :
    print ( "Too big for us, sorry!")
elif area < 5:
    print ( "Too small for us, sorry!")
else:
    cp = calcprice(area,10)  ## which version of calcprice is used : the one in the child (override)
