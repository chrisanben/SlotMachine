# Source File Name: slot_machine.py
# Author's Name: Chris Bentley
# Last Modified By: Chris Bentley
# Date Last Modified: June 04, 2013
""" 
    PROGRAM DESCRIPTION: It is a Python program that takes a users bet as input and given
                        a random output based on probability, the end result will most likely end
                        in the user running out of money to bet.
                        
    VERSION 0.1: Used Tom's Slot Machine Program and made small modifications in the reels.
    
"""

# import statements
import random

def Reels():
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,64,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=18:   # 40.10% Chance
            Bet_Line[spin] = "Rot"
        if Outcome[spin] >= 19 and Outcome[spin] <=28:  # 16.15% Chance
            Bet_Line[spin] = "Durian"
        if Outcome[spin] >= 29 and Outcome[spin] <=36:  # 13.54% Chance
            Bet_Line[spin] = "Seeds"
        if Outcome[spin] >= 37 and Outcome[spin] <=43:  # 11.98% Chance
            Bet_Line[spin] = "Berries"
        if Outcome[spin] >= 44 and Outcome[spin] <=49:  # 7.29%  Chance
            Bet_Line[spin] = "Carrot"
        if Outcome[spin] >= 50 and Outcome[spin] <=54:  # 5.73%  Chance
            Bet_Line[spin] = "Dragon Fruit"
        if Outcome[spin] >= 55 and Outcome[spin] <=58:  # 3.65%  Chance
            Bet_Line[spin] = "Cooked Egg"  
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 3.65%  Chance
            Bet_Line[spin] = "Honey Ham"  
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Waffles"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Taffy"    
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Food_Reel = Reels()
    Food = Food_Reel[0] + " - " + Food_Reel[1] + " - " + Food_Reel[2]
    
    # Match 3
    if Food_Reel.count("Durian") == 3:
        winnings,win = Bet*2,True
    elif Food_Reel.count("Seeds") == 3:
        winnings,win = Bet*5,True
    elif Food_Reel.count("Berries") == 3:
        winnings,win = Bet*10,True
    elif Food_Reel.count("Carrot") == 3:
        winnings,win = Bet*25,True
    elif Food_Reel.count("Dragon Fruit") == 3:
        winnings,win = Bet*50,True
    elif Food_Reel.count("Cooked Egg") == 3:
        winnings,win = Bet*100,True
    elif Food_Reel.count("Honey Ham") == 3:
        winnings,win = Bet*250,True
    elif Food_Reel.count("Waffles") == 3:
        winnings,win = Bet*500,True
    elif Food_Reel.count("Taffy") == 3:
        print("TAFFY!!")
        winnings,win = Bet*1000,True
    
    # Match 2
    elif Food_Reel.count("Rot") == 0:
        if Food_Reel.count("Durian") == 2:
            winnings,win = Bet/2,True
        if Food_Reel.count("Seeds") == 2:
            winnings,win = Bet*1.5,True
        elif Food_Reel.count("Berries") == 2:
            winnings,win = Bet*2,True
        elif Food_Reel.count("Carrot") == 2:
            winnings,win = Bet*3,True
        elif Food_Reel.count("Dragon Fruit") == 2:
            winnings,win = Bet*5,True
        elif Food_Reel.count("Cooked Egg") == 2:
            winnings,win = Bet*10,True
        elif Food_Reel.count("Honey Ham") == 2:
            winnings,win = Bet*25,True
        elif Food_Reel.count("Waffles") == 2:
            winnings,win = Bet*50,True
        elif Food_Reel.count("Taffy") == 2:
            winnings,win = Bet*100,True
    
        # Match Lucky Seven
        elif Food_Reel.count("Taffy") == 1:
            winnings, win = Bet*5,True
            
        else:
            winnings, win = Bet,True
            
    if win:    
        print(Food + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Food + "\nPlease try again. \n")
    
    return Player_Money, Jack_Pot, win

def main():
    """ The Main function that runs the game loop """
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    # Flag to initiate the game loop
    KeepGoing = True
    
    while KeepGoing == True:
        win = 0
        # Give the player some money if he goes broke
        if Player_Money <1:
            input("You have no more money. Here is $500 \nPress Enter\n")
            Player_Money = 500
        
        # User Input
        Prompt = raw_input(" Place Your Bet ! \n Jackpot $ " + str(Jack_Pot) + "\n Money $ " + str(Player_Money) + "\n Q = quit \n")
        if Prompt  == "q" or Prompt  == "Q":
            KeepGoing = False
            break
        
        if Prompt == "" and Turn >1:
            Bet = Prev_Bet
            print("Using Previous Bet")
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        elif is_number(Prompt ):
            Bet = int(Prompt )
            # not enough money
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
                
            # Let's Play
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        # determine win/loss ratio for debugging purposes
        if win:
            win_number += 1
        else:
            loss_number += 1
        win_ratio = "{:.2%}".format(win_number / Turn)
        print("Wins: " + str(win_number) + "\nLosses: " + str(loss_number) + "\nWin Ratio: " + win_ratio + "\n")           
                
    
    #The End
    print("- Program Terminated -")
    
if __name__ == "__main__": main()
