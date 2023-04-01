
### unknown number of input parameters

def printHobbies(name,  *hobbies):
    print ('--name', name)
    mylist = list(hobbies)
    print ( type(hobbies) , type(mylist))
    for hobby in mylist: 
        print ( hobby )







########################
printHobbies('John',  'swimming', 'Reading') 
printHobbies('Peter', 'a', 'b', 'c') 
printHobbies('Paul', 'Reading', 'Swim', 'Run') 
printHobbies('Mike', 'manager', 'Reading','Cards', 'Movies', 'Cooking', 'walking') 


