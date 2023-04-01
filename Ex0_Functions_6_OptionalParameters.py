##### all function definitions

def LargestNumb( a, b ):
    if a > b:
        print (a, "is  bigger  ")
    else: 
        print (a, "is smaller")

def LargestNumb_2( a, b ):
    largest = 0
    if a > b:
        largest = a
    else: 
        largest = b
    return largest

def substract1( a, b ):  		#defining a function
    aminusb = a - b
    print ("The area is" ,aminusb)


################### width is optional, with deault of 2
def calcarea( length, width = 2):  		#defining a function
    area = length * width
    print ("The area is" ,area)
    
################### width is optional with deault 2, depth is optional with default None
def calcproduct( length, width = 2 , depth = None): #default values, depth optional
    if depth == None : 
        area = length * width 
    else: 
        area = length * width * depth
    print ("The area is" ,area)


##################################
print('--- LargestNumb')
LargestNumb(7,5)

print('--- LargestNumb_2')
LargestNumb_2( -6,5)
l = LargestNumb_2( 7,5)
print (l, " is bigger" )

print('--- substract1')
substract1( b=2, a=10)
substract1( 10, 2 )
substract1( 2, 10)

print('--- calcproduct')
calcproduct(length = 7, width = 2 , depth = 3)
calcproduct(7,2,3) 
calcproduct(7, 3) # matches length and width
calcproduct(7, depth = 3) # matches length and depth
# calcproduct( width = 7, depth = 3) # supplying length is compulsory
calcproduct( 7) # supplying length is compulsory






""" create a function
input parameters : a , b
find out which value is bigger
return the biggest number


"""
