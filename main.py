#expeense tracker 
#we import the libreries we need
from datetime import datetime
import csv
from csv_manager import initiator, read_csv, save_data
import pandas as pd
print("welcome to your expense tracker.")
initiator()

print("=Register your expense please=")
#it gets each parameter of the funtion to save it later
name = input("Please type the name of your expense: \n")
amount = float(input("Plase write how much money you expended: \n"))
category = input("Choose a category: Transport \n Food \n Hobbies \n Emergencies \n shopping: \n")
time =  input("Fecha (YYYY-MM-DD): \n")
description = input("please give a short description that explain your expense \n")

expense = {
    'name' : name,
    'amount' : amount,
    'category' : category,
    'time': time,
    'description': description
}

save_data(expense)
print("your expense has been saved!")