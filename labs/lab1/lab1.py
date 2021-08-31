"""
Name: <Hugo Bachaumard>
lab1.py

Problem: This function calculates the area of a rectangle
"""
def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area=", area)

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area=", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume=", volume)

def shooting_percentage():
    total_shots = eval(input("Enter total shots: "))
    shots_made = eval(input("Enter total shots made: "))
    percentage = shots_made/total_shots
    print("Shooting Percentage=", percentage)

def coffee():
    coffee_pounds = eval(input("Enter Pounds of Coffee"))
    total_cost = (coffee_pounds*10.50)+(coffee_pounds*0.86)+1.5
    print("Total Cost of Shipping", total_cost)

def kilometers_to_miles():
    kilometers = eval(input("Enter Amount of Kilometers"))
    total_miles = (kilometers/1.61)
    print("Total Miles", total_miles)

