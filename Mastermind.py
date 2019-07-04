# Program Mastermind 
# Description: 
#   This program recreates the boardgame "Mastermind" 
# Author: Juan Gonzalez
# Date: 03/15/16
# Revised: 
#       03/20/16
#       03/21/16
#       03/25/16
#       03/26/16
#       03/27/16
#       04/01/16
#       04/02/16
#       04/03/16
#       04/13/16
#       04/14/16
#       04/15/16
#       04/16/16
#       04/17/16
#       04/18/16
#       04/19/16
#       04/20/16
#	04/22/16
#       04/25/16
#       04/27/16
#       04/28/16
#       05/04/16
#       05/06/16
#       05/11/16
# list libraries used
import random
import time
import os

os.system('mode con: cols=80 lines=40')
# Declare global constants
LVL1_TURNS = 15
LVL2_TURNS = 10
LVL3_TURNS = 8

LVL1_MULTIPLIER = 8.5
LVL2_MULTIPLIER = 8.5
LVL3_MULTIPLIER = 8.5

LVL1_FLATPOINTS = 50
LVL2_FLATPOINTS = 150
LVL3_FLATPOINTS = 500

LVL1_REDUCING_MULTIPLIER = 0.5
LVL2_REDUCING_MULTIPLIER = 0.5
LVL3_REDUCING_MULTIPLIER = 0.5

LIMIT1 = 6
LIMIT2 = 7

#Main Program



def main():

    
    
    #Declare Local Variables
    lvl = 0
    hints = 0
    points = 0
    leave = ""
    start = ""
    play = ""
    

    intro()
    
    name_lvl_points_hints  = StartMenu()

    name = name_lvl_points_hints[0]

    lvl = name_lvl_points_hints[1]

    points = name_lvl_points_hints[2]

    hints = name_lvl_points_hints[3]

    while (leave != "y"):

        
        print("\n",name,"\tLevel: ",lvl,"\tPoints: ", points,"\tHints: ",hints,"\n",sep="")

        start = input("1 Play\n2 Options\n")

        

        if (start == "1"):
            

            #Separate which levels will be displayed as "Locked" Depending on the players level
            if (lvl == "1"):
                

                print("Select the level you would like to play: ")

                play = input("Level 1 \nLevel 2 (Locked)\nLevel 3 (Locked)\nBack\n")
                

                if (play == "1") or (play == "Level 1") or (play == "level 1"):
                    
                    points_hints = lvl_play(hints, LVL1_TURNS, LVL1_MULTIPLIER, LVL1_FLATPOINTS,LIMIT1, LVL1_REDUCING_MULTIPLIER)

                    points += points_hints[0]

                    hints = points_hints[1]
                    
                
                elif (play == "2") or (play == "Level 2") or (play == "level 2"):
                	
                    input("You have not unlocked this level yet!...")
                    

                elif (play == "3") or (play == "Level 3") or (play == "level 3"):

                    input("You have not unlocked this level yet!...")

                #End If

            


            elif (lvl == "2"):
                

                play = input("Level 1 \nLevel 2 \nLevel 3 (Locked)\nBack\n")
                
                #Depending on the level selected we provide the proper parameters to the lvl function
                if (play == "1") or (play == "Level 1") or (play == "level 1"):

                    points_hints = lvl_play(hints, LVL1_TURNS, LVL1_MULTIPLIER, LVL1_FLATPOINTS, LIMIT1, LVL1_REDUCING_MULTIPLIER)

                    points += points_hints[0]

                    hints = points_hints[1]
                    

                elif (play == "2") or (play == "Level 2") or (play == "level 2"):

                    points_hints = lvl_play(hints, LVL2_TURNS, LVL2_MULTIPLIER, LVL2_FLATPOINTS, LIMIT1, LVL2_REDUCING_MULTIPLIER)

                    points += points_hints[0]

                    hints = points_hints[1]

                elif (play == "3") or (play == "Level 3") or (play == "level 3"):

                    input("You have not unlocked this level yet!...")

                #End If
                

            elif (lvl == "3"):

                play = input("Level 1 \nLevel 2 \nLevel 3\nBack\n")

                if (play == "1") or (play == "Level 1") or (play == "level 1"):

                    points_hints = lvl_play(hints, LVL1_TURNS, LVL1_MULTIPLIER, LVL1_FLATPOINTS, LIMIT1, LVL1_REDUCING_MULTIPLIER)

                    points += points_hints[0]

                    hints = points_hints[1]
                    
                elif (play == "2") or (play == "Level 2") or (play == "level 2"):

                    points_hints = lvl_play(hints, LVL2_TURNS, LVL2_MULTIPLIER, LVL2_FLATPOINTS, LIMIT1, LVL2_REDUCING_MULTIPLIER)

                    points += points_hints[0]

                    hints = points_hints[1]
                    
                elif (play == "3") or (play == "Level 3") or (play == "level 3"):

                    points_hints = lvl_play(hints,LVL3_TURNS,LVL3_MULTIPLIER,LVL3_FLATPOINTS, LIMIT2, LVL3_REDUCING_MULTIPLIER)

                    points += points_hints[0]

                    hints = points_hints[1]

                #End If

            else:

                input("Please enter a valid Choice...")

            #End If
            
                    
                    
        elif (start == "2"):

            
        	
            #Display the user information
            print("\n",name,"\tLevel: ",lvl,"\tPoints: ", points,"\tHints: ",hints,"\n",sep="")

            		
            print("1 Level Up \n2 Buy Hints \n3 Save and Quit \n4 Back")
			
            option = input()
			
            if (option == "1"):
				
                if (lvl == "1"):
					
                    
                    print("Level 1 ", points,"/400", sep = "")
					
                    if (points >= 400):
						
                        up = input("Level up for 400 points?(Y/N)")
						
                        if (up == "y") or (up == "Y"):
							
                            points -= 400
                            lvl = "2"


			#End If
                            
                    else:
						
                        input("You dont have enough points...")

                    #End If
			


				
                elif (lvl == "2"):
					
                    
                    print("Level 2 ", points,"/1000", sep = "")
					
                    if (points >= 1000):
						
                        up = input("Level up for 1000 points?(Y/N)")
						
                        if (up == "y") or (up == "Y"):
							
                            points -= 1000
                            lvl = "3"

                        #else:

                            #Nothing

                        #End If
						
                    else:
						
                        input("You dont have enough points...")

                    #End If


                elif (lvl == "3"):
					
                    
                    print("You are at the maximum Level!...")

                #End If
					


            elif (option == "2"):

                points_purchase = buy_hints(points)

                points = points_purchase[0]
                
                purchase = points_purchase[1]

                hints += purchase
                
            elif (option == "3"):
            	
            	savedData = open('Data.txt', 'w')
            	
            	savedData.write(name + "\n")
            	
            	savedData.write(str(lvl) + "\n")
            	
            	savedData.write(str(points) + "\n")
            	
            	savedData.write(str(hints) + "\n")
            	
            	savedData.close()

            	leave = "y"


            #End If

        #End If

    #End While
        





# Function StartMenu
# Description:
#
#   Lets the user start a new game, load a previous one or read the instructions
#   
# Calls:
#   intructions
# Parameters:
#   none
# Returns:
#   list name_lvl_points_hints


def StartMenu():

    #Declare local variables
    lvl = 0
    hints = 0
    points = 0
    confirm = ""

    
    while (confirm != "y") and (confirm != "Y"):
        
        option = input("1 Start a new game \n2 Load previous game\n3 Instructions\n")
        
        if (option == "1"):
            
            confirm = input("Attention: If you already have a previous game saved your data will be erased. Do you still want to continue?(y/n)")


            if (confirm == "yes") or (confirm == "YES"):

                confirm = "y"

            #End If
                
            if (confirm == "y") or (confirm == "Y"):
                
                name = input("Enter your name: ")
                print("\nWelcome to Mastermind ", name,"!",sep="")
                
                savedGame = open('Data.txt','w')

                lvl = "1"
                points = 0
                hints = 0
                
                savedGame.write(name + "\n")

                savedGame.write(str(lvl) + "\n")

                savedGame.write(str(points) + "\n")

                savedGame.write(str(hints) + "\n")
                
                savedGame.close()

            #End If
                

        elif (option == "2"):

            try:

                savedGame = open('Data.txt','r')

                name = savedGame.readline().rstrip("\n")

                if name == "":

                    print("You dont have any file saved!")

                else:

                    print("Your last saved Data is from \"",name,"\" Do you want to load this file?",end = "", sep = "")

                    confirm = input("(y/n)")

                    if (confirm == "yes") or (confirm == "YES") or (confirm == "Yes"):

                        confirm = "y"
                    

                    if (confirm == "y") or (confirm == "Y"):

                        lvl = savedGame.readline().rstrip("\n")

                        points = savedGame.readline().rstrip("\n")

                        hints = savedGame.readline().rstrip("\n")



                        try:
                            points = float(points)
                            hints = int(hints)

                        except:

                            input("The File is corrupt! Please create a new one...")
                            confirm = "n"

                        savedGame.close()

            except:

                    input("There is no existing file!...")
                          

        elif (option == "3"):

            instructions()
                
 
        else:

             print("Select a valid choice!")

        #End If

    #End While
    name_lvl_points_hints = [name, lvl, points, hints]
    
    return name_lvl_points_hints
    #return name, lvl, points, hints

# Function generate_numbers
# Description:
#   This function generates 4 random numbers that will be
#       the code that the end user has to crack
# Calls:
#   none
# Parameters:
#   Integer limit
# Returns:
#   integer code

def generate_numbers(limit):


    #Declare local variables
    count = 0
    pc = [0,0,0,0]
    code = ""

    for count in range(0,4):

    #We generate each digit seperatly and add them to the full code
    #So that we can return the full 4 digit code as one value
        pc[count] = str(random.randint(1,limit))

        code += pc[count]
        
    
    
    return code
    



#End Function generate_numbers


# Function validateGuess
# Description:
#       Gets the guess from the end user and validates that under correct
#       format as specified in instructions
#       
# Calls:
#   none
# Parameters:
#   string guess, Integer limit
# Returns:
#   Boolean

def validateGuess(guess,limit):

    #Declare local variables
    
    noLetters = ""
    fourDigits = ""
    color = dict()
    counter = 0
    inRange =""
    valid = 0

       
                
    try:

        guess = int(guess)
        valid += 1

    

        if (guess > 9999) or (guess < 1000):

            print("Please enter a 4 digit number between 1 and 6")

                          

        else:

            guess = str(guess)
            valid += 1


            #we assign each digit of the guess to a separate variable
            counter = 0
            for digit in str(guess):

                counter += 1

                digit = int(digit)

                color[counter] = digit

            #So we now have color[1],color[2],etc.. with each digit of the guess

            #We check if each digit is between 1 and 6 or 1 through 7 depending on the level limit

            if limit == 6:
                
                if (color[1] < 1) or (color[1] > 6) or (color[2] < 1) or (color[2] > 6) or (color[3] < 1) or (color[3] > 6) or (color[4] < 1) or (color[4] > 6):
                                                        
                    print("Please enter only digits from 1 through 6")

                else:

                    valid += 1

            if limit == 7:

                if (color[1] < 1) or (color[1] > 7) or (color[2] < 1) or (color[2] > 7) or (color[3] < 1) or (color[3] > 7) or (color[4] < 1) or (color[4] > 7):
                                                        
                    print("Please enter only digits from 1 through 7")
                                
                                
                else:

                    valid += 1

    except ValueError:

        print("That's not a number!")
                        
                            
    if (valid == 3):

        return True

    if (valid < 3):

        return False

               
#End function validateGuess()




# Function giveFeedback
# Description:
#
#       Compares the guess with the code and gives feedback
#       to the end user to let him know if he guessed any numbers
#       in the right position, wrong position or none
# Calls:
#   none
# Parameters:
#   string guess, string code
# Returns:
#   string feedback

def giveFeedback(guess, code):

    #Declare variables
    digit = ""
    counter = 0
    counter2 = 0
    color = dict()
    pc = dict()
    asteriskCount = 0
    poundCount = 0



    #First we assign each digit of the guess to a separate variable

    for digit in str(guess):

        counter += 1

        

        color[counter] = digit

    #So we now have color[1],color[2],etc.. with each digit of the guess

    counter = 0
    for digit in str(code):

        counter += 1

       

        pc[counter] = digit
        


    if (guess == "Hint"):

            see = random.randint(1,4)
            counter = 0

            for counter in (1,2,3,4):

                if counter != see:

                    pc[counter] = "x"

            result = pc[1] + pc[2] + pc[3] + pc[4]




            
    else: 


        #We compare for correct number in correct position
        for counter in (1,2,3,4):


            if (pc[counter] == color[counter]):

                asteriskCount += 1

                pc[counter] = 0
                color[counter] = 7

        

            

        #We check for correct numbers in wrong position
        for counter in (1,2,3,4):

            for counter2 in (1,2,3,4):

                #Make sure it only checks when the position is not the same
                #example: pc[1] and color[1] were already tested 
                if counter != counter2:

                    if pc[counter] == color[counter2]:
                       
                        pc[counter] = 0

                        color[counter2] = 7

                        poundCount += 1

      

        #Since we want to fit it in the box, we make sure that no matter
        #how many pounds and asterisks we got, the feedback will always
        #be 4 spaces long
        
        spaces = (4 - (asteriskCount + poundCount)) * " " 

        asterisk = asteriskCount * "*"
        pound = poundCount * "#"

       



        result = (asterisk) + (pound) + spaces

        #Now we print the results next to the guess


    
    
    return result

#End Function giveFeedback



# Function lvl_play
# Description:
#
#       This function represents lvl 1 of the game
#
# Calls:
#   none
# Parameters:
#   hints , turns, multiplier,flat_points
# Returns:
#   hints, points


def lvl_play(hints,turns, multiplier,flat_points, limit, reduce):

    
#Declare local Variables
    code = 0
    guess = 0
    feedback = 0
    top = ""
    bottom = ""
    turn = 0
    counter = 0
    color = ""
    box = ""
    points = 0
    go = ""
    count = 0
    only_hint = 0
    
    
    #If the user has hints available, he will only have one available per game
    if (hints >= 1):
    	
    	only_hint += 1
    

    #First we generate 4 random numbers between 1 and 6 to be the code
    code = generate_numbers(limit)
    count = 1
    #print(code)


    #Then we set the amount of turns the user has
    
    color = dict()
    while turn < turns:

        go = False
        
        while not(go):
            
            #We get the guess from the user
            guess = input("Enter your guess: ")

            if (guess == "hint"):
    	
                    guess = "Hint"
            
            if (guess == "Hint"):
                
                if (only_hint == 0):
					
                    input("You dont have any hints remaining or already used one in this game...")
				
                else:

                    hints -= 1
                    only_hint = 0
                    go = True
                

            else: 

                go = validateGuess(guess, limit)

        

        #separate each digit from the guess
        counter = 0
        
        for digit in str(guess):

            counter += 1

            color[counter] = digit

            #Get the result from the guess
        result = giveFeedback(guess,code)


        #check if guess is correct or not
        if result != "****":

            turn += 1
            count += 1
            
            multiplier -= reduce

        else:

            turn = turns + 1

                
        #Set our box to draw itself with the guess and the result
                
        top = "╔══╦══╦══╦══╦════╗"
            
        bottom = "╚══╩══╩══╩══╩════╝"


        box += "\n║" + str(color[1]) +" ║" + str(color[2]) +" ║" + str(color[3]) + " ║" + str(color[4]) + ' ║' + str(result) + "║"
        print(top,end="")

        print(box)
        print(bottom)


            

  
    if turn == turns:

        print("The code is unbreakeable!",code)
        points = 0

    if turn == turns + 1:

        
        
        points = flat_points * multiplier
        print("Congratulations! You broke the code in",count,"turns!")
        print("You earned", points,"points")

       
    
    points_hints = [points, hints]
    
    return points_hints

#End function lvl_play



# Function instructions
# Description:
#
#       Shows instructions to understand the game and how it works
# Calls:
#   none
# Parameters:
#
#   None
#   
# Returns:
#
#   None

def instructions():


    tutor = ["","","","","","","","","","","","","","","",""]
    
    tutor[0] = """\nHello! welcome to the tutorial, first thing you should know is why is this text stuck on your screen right now? Well that would be because each time you see "..." at the end of a line it means we are waiting for you to press Enter to continue..."""
    
    tutor[1] = """\nIf you are lazy and found yourself bored with this tutorial you can always enter \"Q\" after any \"...\" to leave..."""
    
    
    
    tutor[2] = """\nOk now we can go into the game basics. Mastermind is originally a boardgame consisting of two players one which creates a code with 4 colors and the other needs to crack that code by guessing multiple times..."""
        
        
            
    tutor[3] = "\nThe code is created out of 6 possible colors and the colors can be repeated inside the code..."
            
            
                
    tutor[4] = "\nIn this program the colors are represented by numbers from 1 through 6 and you are playing against the computer..."
                
                
                    
    tutor[5] = "\nAs soon as you start a game, the computer will generate a code of 4 digits and each digit can be between 1 and 6...(on the first and second level)"
                    
                    
                        
    tutor[6] = """\nAfter this, a message saying \"Enter your guess:\" will appear and you will enter your 4 digit number with all digits between 1 and 6. Example: \"Enter your guess: 2345\"..."""
                        
                        
                            
    tutor[7] = """\n\nAfter receiving your answer we will check how many numbers you got correct and on the right position, and how many did you get correct but in the wrong position, oh what an easy game right?..."""
                            
                            
                                
    tutor[8] = " \nBut the tricky part is that we do not tell you which ones are they ..."
                                
                                
                                    
    tutor[9] = """   \nFor each number that you have in the right position the computer will show you a star \'*\'
 Example:╔══╦══╦══╦══╦════╗
         ║1 ║2 ║5 ║5 ║**  ║ (code: 1234)
         ╚══╩══╩══╩══╩════╝
                                    
   This is how the game looks after you enter a guess. The 1234 would be the guess entered by the player and the box to the right of the guess will always show you feedback about your guess. In this example we see that it gave us two stars this means we got two numbers in the right position as we can see that the 2 and the 4 are correct..."""
                                    
                                    
                                        
    tutor[10] = """   \nFor each number that you got right but in the wrong position the computer will show you a pound\'#\' 
 Example:╔══╦══╦══╦══╦════╗
         ║4 ║3 ║2 ║1 ║####║ (code: 1234) 
         ╚══╩══╩══╩══╩════╝
                                                    
   In this example we can see how all the numbers guessed are inside the code, but all in the wrong position so we would get 4 pounds"""
                                        
                                        
                                            
    tutor[11] = """In the first level you will get 15 tries to guess the code correctly and each time you enter a guess they get added to the box so you can check your previous guesses with no problem.
                                                
 Example:╔══╦══╦══╦══╦════╗
         ║5 ║2 ║3 ║3 ║####║
         ║2 ║2 ║2 ║2 ║*   ║
         ╚══╩══╩══╩══╩════╝..."""

    tutor[12] = """This is a list of the information of every level:

Level 1: 15 Turns, Digits from 1 to 6

Level 2: 10 Turns, Digits from 1 to 6

Level 3: 8 Turns, Digits from 1 to 7"""

                                    

    tutor[13] = "You can level up by earning points each time you win a game, which you can spend to level up or to buy hints. Using a hint will show you one of the numbers inside the code..."

    tutor[14] = "You can only use one hint per game no matter how many hints you have. To use a hint type \"Hint\" in a game and you will receive a number of the code in its correct position..."
    

    
                                            
    x = 0
    answer = ""
    while (answer != "q")  and (x < 14):

        print(tutor[x])
        answer = input()
        x += 1
        if answer == "Q":
            answer = "q"


#End Function intructions


# Function buy_hints
# Description:
#
#       Gives the option to the end-user to buy hints
# Calls:
#   none
# Parameters:
#
#   Float points
#   
# Returns:
#
#   list remaining_purchase

def buy_hints(points):


    #Declare local variables
    leave = ""
    purchase = 0
    subtotal = 0
    remaining = 0

    while leave != "y":
        
        print("\nPoints available:",points,"\n1 Hint = 500 Points")
        
        purchase = input("\nHow many hints would you like?(0 to leave): ")

        try:

            purchase = int(purchase)

            subtotal = purchase * 500

            if points < subtotal:

                input("You dont have enough points!...")

            elif subtotal < 0:

                input("That is not a valid amount!...")

            else:
            
                remaining = points - subtotal
                leave = "y"

                remaining_purchase = [remaining, purchase]
                return remaining_purchase

        except:

            input("Please enter a valid amount!...")

        

# Function instructions
# Description:
#
#       Displays the introduction animation
# Calls:
#   none
# Parameters:
#
#   None
#   
# Returns:
#
#   none

def intro():




    


    time.sleep(0.5)
    print("""\n




██╗   ███╗
███╗ ████║
█╔████╔██║
█║╚██╔╝██║
█║ ╚═╝ ██║
═╝     ╚═╝
           


\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    time.sleep(0.5)
    print("""





██╗   ███╗ █████╗ 
███╗ ████║██╔══██╗
█╔████╔██║███████║
█║╚██╔╝██║██╔══██║
█║ ╚═╝ ██║██║  ██║
═╝     ╚═╝╚═╝  ╚═╝
                   
           


\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    time.sleep(0.5)
    print("""





██╗   ███╗ █████╗ ██████╗
███╗ ████║██╔══██╗█╔════╝
█╔████╔██║███████║██████╗
█║╚██╔╝██║██╔══██║╚════█║
█║ ╚═╝ ██║██║  ██║██████║
═╝     ╚═╝╚═╝  ╚═╝╚═════╝
                           


           
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    time.sleep(0.5)
    print("""





██╗   ███╗ █████╗ ██████╗████████╗
███╗ ████║██╔══██╗█╔════╝╚══██╔══╝
█╔████╔██║███████║██████╗   ██║   
█║╚██╔╝██║██╔══██║╚════█║   ██║   
█║ ╚═╝ ██║██║  ██║██████║   ██║   
═╝     ╚═╝╚═╝  ╚═╝╚═════╝   ╚═╝   
                                    


           
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    time.sleep(0.5)
    print("""





██╗   ███╗ █████╗ ██████╗████████╗██████╗
███╗ ████║██╔══██╗█╔════╝╚══██╔══╝██╔═══╝
█╔████╔██║███████║██████╗   ██║   ████╗  
█║╚██╔╝██║██╔══██║╚════█║   ██║   ██╔═╝  
█║ ╚═╝ ██║██║  ██║██████║   ██║   ██████╗
═╝     ╚═╝╚═╝  ╚═╝╚═════╝   ╚═╝   ╚═════╝
                                            


           
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    time.sleep(0.5)
    print("""




██╗   ███╗ █████╗ ██████╗████████╗██████╗██████╗ 
███╗ ████║██╔══██╗█╔════╝╚══██╔══╝██╔═══╝██╔══██╗
█╔████╔██║███████║██████╗   ██║   ████╗  ██████╔╝
█║╚██╔╝██║██╔══██║╚════█║   ██║   ██╔═╝  ██╔══██╗
█║ ╚═╝ ██║██║  ██║██████║   ██║   ██████╗██║  ██║
═╝     ╚═╝╚═╝  ╚═╝╚═════╝   ╚═╝   ╚═════╝╚═╝  ╚═╝
                                                    


           
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")


    time.sleep(1.5)
    print("""

██╗   ███╗ █████╗ ██████╗████████╗██████╗██████╗ ███╗   ███╗██╗███╗   ██╗█████╗ 
███╗ ████║██╔══██╗█╔════╝╚══██╔══╝██╔═══╝██╔══██╗████╗ ████║██║████╗  ██║██╔══█╗
█╔████╔██║███████║██████╗   ██║   ████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║██║  █║
█║╚██╔╝██║██╔══██║╚════█║   ██║   ██╔═╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██║  █║
█║ ╚═╝ ██║██║  ██║██████║   ██║   ██████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║█████╔╝
═╝     ╚═╝╚═╝  ╚═╝╚═════╝   ╚═╝   ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚════╝ 



\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

    time.sleep(0.5)
    print("""

██╗   ███╗ █████╗ ██████╗████████╗██████╗██████╗ ███╗   ███╗██╗███╗   ██╗█████╗ 
███╗ ████║██╔══██╗█╔════╝╚══██╔══╝██╔═══╝██╔══██╗████╗ ████║██║████╗  ██║██╔══█╗
█╔████╔██║███████║██████╗   ██║   ████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║██║  █║
█║╚██╔╝██║██╔══██║╚════█║   ██║   ██╔═╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██║  █║
█║ ╚═╝ ██║██║  ██║██████║   ██║   ██████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║█████╔╝
═╝     ╚═╝╚═╝  ╚═╝╚═════╝   ╚═╝   ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚════╝ 


By Juan Gonzalez

\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

main()


