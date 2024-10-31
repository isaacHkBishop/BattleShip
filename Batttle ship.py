import random

# Function to create a 2D array
def createArr(rows, cols):
    # Initialize a 2D array with zeros
    array = []
    for i in range(rows):
        row = []  # Create a new row
        for j in range(cols):
            row.append(0)  # Fill the row with zeros
        array.append(row)  # Add the row to the 2D array
    return array

#Battle ship game
#for x in range(5):
#  for c in range(5):
#    ray[x][c].append(0)
#makes were the ship is/the place were they nead the shot to hit
ranOne = random.randint(0, 4)
ranTwo = random.randint(0, 4)
#this is the "ocaen"/ were the ships are
ocean = [[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
#made the loop
ships = 1
#see if the user wants to make there own size ocean
hold = input(print("do you want to make the size of the ocean? YES or NO"))
#if hold == "YES" or hold == "yes" or hold == "NO" or hold == "no":
#while(hold == "YES" or hold == "yes" or hold == "NO" or hold == "no"):
#    hold = input(print("please say yes or no"))
#if no we use the pre made one
if hold == "NO" or hold == "no":
    while(ships != 0):
#prints the ocaen
        for x in ocean:
            print(x)
#takes the user input
        print("where would you like to take a shot at it's a 5 by 5 grid")
        userOne = int(input("what row do you want to hit?"))
        userTwo = int(input("what colum do you want to hit?"))
#checks to see if its in the range
        if userOne < 6 and userOne > 0 and userTwo < 6 and userTwo > 0:
            if ranOne == userOne -1 and ranTwo == userTwo -1:
                print("hit")
                ships -= 1
            else:
                ocean[userOne -1][userTwo -1] = "X"
                print("miss")
#if the user shot is not in range re do
        else:
            print("pleas have your number range from 1 to 5")
            userOne = int(input("what row do you want to hit?"))
            userTwo = int(input("what colum do you want to hit?"))
            if ranOne == userOne -1 and ranTwo == userTwo -1:
                print("hit")
                ships -= 1
            else:
                ocean[userOne -1][userTwo -1] = "X"
                print("miss")
#win
        if ships == 0:
            print("you win")
#if yes they make there own
else:
# Create the 2D array
    rows = int(input("How many rows do you want to have? "))
    cols = int(input("How many columns do you want to have? "))
    newOcean = createArr(rows, cols)
    ranOne = random.randint(0, rows -1)
    ranTwo = random.randint(0, cols -1)
    #ships = 1
    while(ships != 0):
#prints the ocaen
        for x in newOcean:
            print(x)
#takes the user input
        print("where would you like to take a shot at it's a " + str(rows) + " by " + str(cols) + " grid")
        userOne = int(input("what row do you want to hit?"))
        userTwo = int(input("what colum do you want to hit?"))
#checks to see if its in the range
        if userOne < rows +1 and userOne > 0 and userTwo < cols +1 and userTwo > 0:
            if ranOne == userOne -1 and ranTwo == userTwo -1:
                print("hit")
                ships -= 1
            else:
                newOcean[userOne -1][userTwo -1] = "X"
                print("miss")
#win
        if ships == 0:
            print("you win")