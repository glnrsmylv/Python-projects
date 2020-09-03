#functions module
from lib import User
from db import db
user_inputs=["Name", "Surname", "Username", "Password"]
def getDataFromUser():
    user_inputs_data = []
    for u_input in user_inputs:
        user_inputs_data.append(input(u_input+" : "))
    return user_inputs_data

def createUserObject():
    return User(*getDataFromUser())
def addUserToDb():
    db.append(createUserObject())
def showAllusers():
    for user in db:
        user.showData()
def showUserByName():
    pass
def programStart():
    if int(input("Type 1 to start: "))==1:
        for count in range(int(input("Add student count : "))):
            count+=1
            print(f" Add new user number {count}")
        addUserToDb()
    showAllusers()
