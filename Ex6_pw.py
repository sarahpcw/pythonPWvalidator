# -*- coding: utf-8 -*-
"""
Create a method:
    input parameters: a string value, and a password
    for every letter in the password, is one of them in the string value, if so retun true else return false
"""


class lib():

    def checkPassword ( self, pw ):
        b = False
        userpw = ''
        count = 0 
        while pw != userpw and count < 3:
            userpw = input("Enter the passsword ")
            count+=1
        if pw == userpw:
             b = True
        return b

    def checkLetters (self , val, pw):
        b = False
        for i in range (0, len(pw), 1) :
            if val.count( pw[i] ) >= 1 :
                b = True
                break
        return b
