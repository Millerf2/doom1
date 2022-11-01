#Miller Fourie, UCID: 30186898, Tutorial Section: 03
#Python Version: 3.8

#Initializing variables
gameLoop = True
error = False
looping = True
newLocation = True
location = "entrance"
doorCondition = "Locked"
silverLockPos = "beginning"
goldLockPos = "beginning"
locationDescription = ""
scrollingTxtDecision = "Undecided"
spaces = "        "
turnNumber = 0

#defines a method to allow for scrollingTxt. Scrolling Text greatly increases the ease of reading / understanding the order of text.
def scrollingTxt(text):
    print(text)
        
#Introduction Text to set a motive and task for the player.
scrollingTxt("""
        BACKGROUND:
        Your walking your habitual walk, when you walk upon a building which lays where your walk used to be.
        While any normal person would walk around, your stubornly dedicated to habit, and thus attempt to walk
        your habitual walking route... through the house. As you enter, you notice that the door you came from 
        has dissapeared, and seemingly moved infront of you. Desperately trying to maintain habit, you begin 
        looking for a way out. The sign above the door tells you that you need to find and unlock a gold and 
        silver lock to escape.
        
        NEW OBJECTIVE: 
        Unlock the door by finding and unlocking the Silver and Gold lock.
        """)

#Doesn't wait if print text option is selected because TA probally doesn't want to read the entire background. 
 


while (gameLoop == True or error == True):
    if(error == False and gameLoop == True):
        turnNumber = turnNumber+1
    gameLoop = False
    error = False
    
    #Sets a variable with the all the required information of each location. In addition,
    #it sets the locationDescription variable, which provides a basic description of the room you enter. 
    if(location == "entrance"):
        locationChoices = f"""
        
        Turn: {turnNumber}
        Current Location: {location}
        -----------------------------
        The Silver lock is currently set to the {silverLockPos} position.
        The Gold lock is currently set to the {goldLockPos} position.
        
        Choices:
        Try to open the door (Press 1)
        Go through the left entryway (To the pantry!) (Press 2)
        Go through the right entryway (To the kitchen!) (Press 3)
        """
        
        locationDescription = ""
       
        
        
    if(location == "pantry"):
        locationChoices =  f"""  
        
        Turn: {turnNumber}
        Current Location: {location}
        -----------------------------
        The Silver lock is currently set to the {silverLockPos} position.
        The Gold lock is currently set to the {goldLockPos} position.
              
        Choices: 
        Turn the silver lock to the left position (Press 1)
        Turn the silver lock to the right position (Press 2)
        Turn the silver lock to the center position (Press 3)
        Don't change the position! Return to entranceway (Press 4)
        """
        locationDescription = spaces+"Following the breadcrumbs on the ground, you find a Silver Lock."

    
    
    if(location == "kitchen"):
        locationChoices = f"""
        
        Turn: {turnNumber}
        Current Location: {location}
        -----------------------------
        The Silver lock is currently set to the {silverLockPos} position.
        The Gold lock is currently set to the {goldLockPos} position.
                
        Choices:
        Turn the gold lock to the left position (Press 1)
        Turn the gold lock to the right position (Press 2)
        Turn the gold lock to the center position (Press 3)
        Don't change the position! Return to entranceway (Press 4)
        """
        
        locationDescription = spaces+"Between the hanging knives in the kitchen, there’s a Golden Lock. "
        
    
    #Purpose: This function makes it so that whenever a player enters a room, they are shown a description. But once in the room, 
    #the description will not repeat with locationChoices (the required information to makes decisions)
    if(newLocation == True):
        scrollingTxt(locationDescription)
        newLocation = False
        
    #Prints locationChoices, which provides the player with the required information to make a decision. 
    scrollingTxt(locationChoices)
        
    #Asks the player for what they want to do.
    print("")
    choice = input(spaces+"What do you want to do?")
    
    #Checks for incorrect type inputs
    try:
        #Tries to cast choice as a int
        choice = int(choice)
        
        #If the player chooses 4 and we are in the entrance, then they did  create an error because all locations except for the entrance have 4 options. In both cases, there are no options below 1.
        if((choice > 3 or choice < 1) and location == "entrance"):
            print(spaces+"Out of range integer value. Try inputting a number between 1 and 3.")
            error = True;
        #If the player chooses 4 and we are not in the entrance, then they did not create an error because all locations except for the entrance have 4 options. In both cases, there are no options below 1.
        elif((choice > 4 or choice < 1) and location != "entrance"):
            print(spaces+"Out of range integer value. Try inputting a number between 1 and 4.")
            error = True;
            
    #If variable choice is not a int, then they input an incorrect variable type.
    except ValueError:
        error = True
        print(spaces+"Incorrect variable type.", end="") #end operator allows as to print on the same line.
        #if statements to provide proper solutions to the error the player is facing.
        if(location == "entrance"):
            print("Try inputting a number between 1 and 3")
        else:
            print("Try inputting a number between 1 and 4")
            
    #Game Loop
    if(error == False):
        gameLoop = True
        
        #Handles the inputs for each location.
        if(location == "entrance"):
            
            if(choice == 1):
                if(doorCondition == "Locked"):
                    scrollingTxt(spaces+"(ACTION) You try to open the door, but it remains stubornly locked.")
                else:
                    scrollingTxt("""
        (ACTION) You try to open the door, and it opens! A gust of wind pushes you out of the house,
        and as you look back, there is nothing but a hole in the ground from where the house used to be. """)
                    quit()
                    
                
            elif(choice == 2):
                scrollingTxt(spaces+"(ACTION) You walk to the left of the entryway, into what appears to be a pantry. ")
                location = "pantry"
                newLocation = True #Whenever a new location is set, newLocation is set to True so that a little description of the new room displays
        
            else:
                scrollingTxt(spaces+"(ACTION) You walk to the right of the entryway, into what appears to be a kicthen. ")
                location = "kitchen"
                newLocation = True

               
                    
        if(location == "pantry"):
            if(choice == 1):
                scrollingTxt(spaces+"(ACTION) You turn the Silver Lock to the left position")
                silverLockPos = "Left"
                
            elif(choice == 2):
                if(newLocation == False):
                    scrollingTxt(spaces+"(ACTION) Turn the silver lock to the right position")
                    silverLockPos = "Right"    
                                        
            elif(choice == 3):
                if(newLocation == False):
                    scrollingTxt(spaces+"(ACTION) Turn the silver lock to the center position")
                    silverLockPos = "Center"
            else:
                scrollingTxt(spaces+"(ACTION)You re-enter the entrance, becoming more anxious to return to your walk.")
                location = "entrance"
                newLocation = True

                 
        elif(location == "kitchen"):
            if(choice == 1):
                scrollingTxt(spaces+"(ACTION) You turn the Gold Lock to the left position")
                goldLockPos = "Left"
            elif(choice == 2):
                scrollingTxt(spaces+"(ACTION) Turn the Gold lock to the right position")
                goldLockPos = "Right"    
                                        
            elif(choice == 3):
                if(newLocation == False):
                    scrollingTxt(spaces+"(ACTION) Turn the Gold lock to the center position")
                    goldLockPos = "Center"
            else:
                scrollingTxt(spaces+"(ACTION)You re-enter the entrance, becoming more anxious to return to your walk.")
                location = "entrance" 
                newLocation = True

        #Checks if the player has won the game or not
        if(silverLockPos == "Right" and goldLockPos == "Left"):
            doorCondition = "Unlocked"
        else: #else statement is placed into the game so that if the player gets the solution, but then changes there solution to an incorrect solution, the locks will remain closed.
            doorCondition = "Locked"   
                        
                    
                        
                    
                
                
      
            
            
        
