#Natalie Gotham
#Game 

import random


print ('Welcome to Camel!')
print ('You have stolen a camel to make your way across the great Mobi desert.')
print ('The natives want their camel back and are chasing you down! Survive your')
print (' desert trek and outrun the natives.')

done = False
playerMilesTraveled = 0
enemyMilesTraveled = -20
enemyDistanceOffset = 0
playerThirst = random.randint(0, 2)
camelTiredness = 0
#generate random initial number of drinks in canteen
canteenDrinksGenerator = random.randint(2, 4)
#storage value to be updated throughout game run
canteenTotalDrinks = canteenDrinksGenerator
nativeWarning = "The natives are getting close!"
oasisMagicNumber = random.randint(1, 20)

#Primary game loop
while not done: 
    
    #defining at the top of the game loop to ensure reset to 0 each turn.
    turnMilesTraveled = 0
    
    #update offset before beginning of each turn
    enemyDistanceOffset = playerMilesTraveled - enemyMilesTraveled

    if enemyDistanceOffset <= 0:
        print ("\nYou were too slow, and the natives have caught you!")
        print ("Your demise is sudden and brutal.")
        print ("Game over!")
        done = True
        break
    
        
     
    if not done and enemyDistanceOffset < 15:
        print("The natives are getting close!")
        
    if not done and camelTiredness >= 5 and camelTiredness < 8:
        print("Your camel is getting tired.")
        
        
    
    #Primary game board
    
    print ("\nA. Drink from your canteen.")
    print ("B. Ahead moderate speed.")
    print ("C. Ahead full speed.")
    print ("D. Stop for the night.")
    print ("E. Status check.")
    print ("Q. Quit.\n")
    
    #Ask the user their choice
    playerChoice = input("Your choice? ")
    
    #printing a newline made it doublespaced but this adds a single line space without making the input line complicated
    print("")
    
    
    #rolls d20 for chance of player finding oasis each turn
    #excludes status check turn so players cant spam it to get an oasis
    findOasis = random.randint(1, 20)

    #Manual exit
    if playerChoice.upper() == "Q":
        print ("Exiting program.")
        done = True    
        
    #chance of finding oasis, prevents finding on first turn
    #excludes status check to prevent player spamming it to get oasis
    if not done and playerChoice.upper() != "E" and playerMilesTraveled > 0 and findOasis == oasisMagicNumber:
        print ("You found an oasis!")
        print ("You drink and fill your canteen,")
        print ("and your camel has rested.")
        playerThirst = 0
        camelTiredness = 0
        #reset canteen drinks to 4 (full)
        canteenTotalDrinks = 4
    

    #user checks status        
    elif playerChoice.upper() == "E":
        print (f"Miles traveled: {playerMilesTraveled}")
        print (f"Drinks in canteen: {canteenTotalDrinks}")
        print (f"The natives are {enemyDistanceOffset} miles behind you.")
        
    #user rests for the night
    elif playerChoice.upper() == "D":
        camelTiredness = 0
        print ("Your camel is well-rested and happy.")
        enemyMilesTraveled += random.randint(7, 14)
        
    #user goes ahead full speed    
    elif playerChoice.upper() == "C":
        turnMilesTraveled += random.randint(10, 20)
        playerMilesTraveled += turnMilesTraveled
        enemyMilesTraveled += random.randint(7, 14)
        playerThirst += 1
        camelTiredness += random.randint(1, 3)
        print ("You choose to forge ahead at full speed.")
        print (f"You have traveled {turnMilesTraveled} miles ahead.\n")
        
    #user goes ahead moderate speed    
    elif playerChoice.upper() == "B": 
        turnMilesTraveled += random.randint(5, 12)
        playerMilesTraveled += turnMilesTraveled
        enemyMilesTraveled += random.randint(7, 14)
        playerThirst += 1
        camelTiredness += 1
        print ("You choose to forge ahead at a moderate pace.")
        print (f"You have traveled {turnMilesTraveled} miles ahead.\n")
        
    #user chooses to drink from canteen
    elif playerChoice.upper() == "A":
        if canteenTotalDrinks > 0:
            #take a drink
            canteenTotalDrinks -= 1
            playerThirst = 0
            print ("You take a drink from your canteen.")
        else:
            print ("You have no water left in your canteen!")
            print ("You pray that you find an oasis soon...")
            
    if not done and playerThirst >= 3 and playerThirst <= 5:
        print ("You are thirsty.")
        
        
    elif playerThirst > 5:
        print ("You have died of thirst.")
        print ("The desert claims another victim.\n")
        print ("Game over!")
        done = True
        
    if camelTiredness > 8:
        print ("Your camel has died.")
        print ("You are doomed to dessicate in the desert sun.\n")
        print ("Game over!")
        done = True    
        
        
    if not done and playerMilesTraveled >= 200 and playerThirst <= 6 and camelTiredness <= 8:
        print ("You made it across the desert, and have won the game!")
        done = True
        break
        
    
print ("\nThank you for playing!")