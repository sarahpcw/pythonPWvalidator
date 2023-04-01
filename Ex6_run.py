# -*- coding: utf-8 -*-
"""
Create a method:
    input parameters: a string value, and a password
    for every letter in the password, is one of them in the string value, if so retun true else return false


"""
#E:\.spyder-py3\.spyder-py3\\DataD1\\MBPlayerSalaries200Sample.csv


from pw import lib
obj = lib();

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
digit = "0123456789"
specialcharacters = "!£$%^&*()@?"

pw  = 'rt56*'

b   = obj.checkPassword(pw)
print("Password enetered correctly: ", b)

lc = obj.checkLetters(lowercase, pw)

uc = obj.checkLetters(uppercase, pw)

d = obj.checkLetters(digit, pw)

spec = obj.checkLetters(specialcharacters, pw)

if lc and uc and d and spec :
    print("\nPassword Valid ")
else: 
    print ("\nPassword invalid")
    print ("----------------")
    print(spec, "spec found ")
    print(d, "digit found ")
    print(lc, "lowercase found ")
    print(uc , "uppercase found ")
