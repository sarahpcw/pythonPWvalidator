class cfunctions ():  # to create class 
    # indent all the functions
    
    def __init__(self,name):
        self.name = name
        
    def printCompanyMessage(self): # self
        print ( "Welcome to  ", self.name , "! Parent Class ")
        
    def printPersonalGreeting(self):
        print ( "Hi , thanks for requesting a quote!" )
        
    def carpetlengthWidth(self):
        w=float(input("Enter width: "))
        h=float(input("Enter height: "))
        return w,h
    
    def calcArea (self, l,w):
        area = l*w
        print ( "Area", area )
        return area

    def calcPrice(self, area): 
        carpetSQMPrice = 15.00
        carpetPrice = carpetSQMPrice * area
        return carpetPrice
     

    def calcTravelFee(self, distance):
       fee =0
       if distance < 10 :
            fee = 0  
       elif distance > 10 and distance< 20 :
            fee = 10
       elif distance > 20 :
             fee = 20
       return fee