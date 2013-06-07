# Source File Name: slot_machine.py
# Author's Name: Chris Bentley
# Last Modified By: Chris Bentley
# Date Last Modified: June 04, 2013
""" 
    PROGRAM DESCRIPTION: It is a Python program that takes a users bet as input and given
                        a random output based on probability, the end result will most likely end
                        in the user running out of money to bet.
                        
    VERSION 0.3: Added A Money and Bet Amount Labels
                    - Bet Labels now display how much user bets
                    - Removed Slot Labels and replaced them as images
                    - Buttons have been move slightly
                    - Imported Berries.png with Transparency

    
"""

# import statements
import random
import ttk
from Tkinter import *
from PIL import Image, ImageTk

class SlotMachine:
    
    def __init__(self, master=None):

        self.buttonFont = "-family Forte -size 22 -weight normal -slant roman -underline 0 -overstrike 0"
        
        # Display the Slot Machine Image on a Canvas Panel
        self.bg_panel = Canvas(master, width=640, height=480, bg="black")
        self.bg_panel.pack(expand=YES,fill=BOTH)       
        self.bg_img = Image.open("images/background.gif")
        self.bg_imgTk = ImageTk.PhotoImage(self.bg_img)
        self.bg_panel.create_image(0, 0, image = self.bg_imgTk, anchor = NW)

        #Display the Reel Slot
        self.reel1_img = Image.open("images/reelslot.gif")
        self.reel1_imgTk = ImageTk.PhotoImage(self.reel1_img)
        self.bg_panel.create_image(200, 150, image = self.reel1_imgTk, anchor = NW)

        #Display the Reel Slot
        self.reel2_img = Image.open("images/reelslot.gif")
        self.reel2_imgTk = ImageTk.PhotoImage(self.reel2_img)
        self.bg_panel.create_image(290, 150, image = self.reel2_imgTk, anchor = NW)

        #Display the Reel Slot
        self.reel3_img = Image.open("images/reelslot.gif")
        self.reel3_imgTk = ImageTk.PhotoImage(self.reel3_img)
        self.bg_panel.create_image(380, 150, image = self.reel3_imgTk, anchor = NW)

        #Import Berries Image
        self.berries_img = Image.open("images/berries.png")
        self.berries_imgTk = ImageTk.PhotoImage(self.berries_img)

        #Display Bet Amount
        self.betAmount = Label (self.bg_panel)
        self.betAmount.place(x=420,y=290,height=35,width=150)
        self.betAmount.configure(background="#000000")
        self.betAmount.configure(borderwidth="0")
        self.betAmount.configure(font=self.buttonFont)
        self.betAmount.configure(foreground="#ff0000")
        self.betAmount.configure(anchor="n")
        self.betAmount.configure(text="0000")

        #Display Bet Label
        self.betLabel = Label (self.bg_panel)
        self.betLabel.place(x=320, y=290, height=35, width=50)
        self.betLabel.configure(background="#000000")
        self.betLabel.configure(borderwidth="0")
        self.betLabel.configure(font=self.buttonFont)
        self.betLabel.configure(foreground="#ff0000")
        self.betLabel.configure(anchor="n")
        self.betLabel.configure(text="Bet:")

        #Display Money Amount
        self.cashAmount = Label (self.bg_panel)
        self.cashAmount.place(x=170,y=290,height=35,width=150)
        self.cashAmount.configure(background="#000000")
        self.cashAmount.configure(borderwidth="0")
        self.cashAmount.configure(font=self.buttonFont)
        self.cashAmount.configure(foreground="#ff0000")
        self.cashAmount.configure(anchor="n")
        self.cashAmount.configure(text="1000")

        #Display Money Label
        self.cashLabel = Label (self.bg_panel)
        self.cashLabel.place(x=60, y=290, height=35, width=100)
        self.cashLabel.configure(background="#000000")
        self.cashLabel.configure(borderwidth="0")
        self.cashLabel.configure(font=self.buttonFont)
        self.cashLabel.configure(foreground="#ff0000")
        self.cashLabel.configure(anchor="n")
        self.cashLabel.configure(text="Cash:")

        # Display the Bet ALL button
        self.betAllButton = Button(self.bg_panel)
        self.betAllButton.place(x=425, y=375, height=46, width=125)
        self.betAllButton.configure(borderwidth="0")
        self.betAllButton_img = PhotoImage(file="images/button.gif")
        self.betAllButton.configure(image=self.betAllButton_img)
        self.betAllButton.configure(cursor="hand2")
        self.betAllButton.configure(font=self.buttonFont, compound="center", text="Bet All")
        self.betAllButton.bind("<Button-1>",self.betALL)

        # Display the Bet 100 button
        self.bet100Button = Button(self.bg_panel)
        self.bet100Button.place(x=300, y=325, height=46, width=125)
        self.bet100Button.configure(borderwidth="0")
        self.bet100Button_img = PhotoImage(file="images/button.gif")
        self.bet100Button.configure(image=self.bet100Button_img)
        self.bet100Button.configure(cursor="hand2")
        self.bet100Button.configure(font=self.buttonFont, compound="center", text="Bet 100")
        self.bet100Button.bind("<Button-1>",self.bet100)

        # Display the Bet 250 button
        self.bet250Button = Button(self.bg_panel)
        self.bet250Button.place(x=425, y=325, height=46, width=125)
        self.bet250Button.configure(borderwidth="0")
        self.bet250Button_img = PhotoImage(file="images/button.gif")
        self.bet250Button.configure(image=self.bet250Button_img)
        self.bet250Button.configure(cursor="hand2")
        self.bet250Button.configure(font=self.buttonFont, compound="center", text="Bet 250")
        self.bet250Button.bind("<Button-1>",self.bet250)

        # Display the Bet 500 button
        self.bet500Button = Button(self.bg_panel)
        self.bet500Button.place(x=300, y=375, height=46, width=125)
        self.bet500Button.configure(borderwidth="0")
        self.bet500Button_img = PhotoImage(file="images/button.gif")
        self.bet500Button.configure(image=self.bet500Button_img)
        self.bet500Button.configure(cursor="hand2")
        self.bet500Button.configure(font=self.buttonFont, compound="center", text="Bet 500")
        self.bet500Button.bind("<Button-1>",self.bet500)

        # Display the Spin button
        self.spinButton = Button(self.bg_panel)
        self.spinButton.place(x=120, y=350, height=46, width=125)
        self.spinButton.configure(borderwidth="0")
        self.spinButton_img = PhotoImage(file="images/button.gif")
        self.spinButton.configure(image=self.spinButton_img)
        self.spinButton.configure(cursor="hand2")
        self.spinButton.configure(font=self.buttonFont, compound="center", text="Spin")
        #self.spinButton.bind("<Button-1>",self.ResetButtonClick)
    
    def bet100(self, event):
        Player_Bet = 100
        self.betAmount["text"] = Player_Bet
        
    def bet250(self, event):
        Player_Bet = 250
        self.betAmount["text"] = Player_Bet

    def bet500(self, event):
        Player_Bet = 500
        self.betAmount["text"] = Player_Bet

    def betALL(self, event):
        Player_Bet = 1000
        self.betAmount["text"] = Player_Bet


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
            winnings,win = Bet*5,True
        elif Food_Reel.count("Seeds") == 3:
            winnings,win = Bet*10,True
        elif Food_Reel.count("Berries") == 3:
            winnings,win = Bet*25,True
        elif Food_Reel.count("Carrot") == 3:
            winnings,win = Bet*50,True
        elif Food_Reel.count("Dragon Fruit") == 3:
            winnings,win = Bet*100,True
        elif Food_Reel.count("Cooked Egg") == 3:
            winnings,win = Bet*200,True
        elif Food_Reel.count("Honey Ham") == 3:
            winnings,win = Bet*400,True
        elif Food_Reel.count("Waffles") == 3:
            winnings,win = Bet*800,True
        elif Food_Reel.count("Taffy") == 3:
            print("TAFFY!!")
            winnings,win = Bet*1000,True
        
        # Match 2
        elif Food_Reel.count("Rot") == 0:
            if Food_Reel.count("Durian") == 2:
                winnings,win = Bet*1,True
            if Food_Reel.count("Seeds") == 2:
                winnings,win = Bet*3,True
            elif Food_Reel.count("Berries") == 2:
                winnings,win = Bet*5,True
            elif Food_Reel.count("Carrot") == 2:
                winnings,win = Bet*10,True
            elif Food_Reel.count("Dragon Fruit") == 2:
                winnings,win = Bet*15,True
            elif Food_Reel.count("Cooked Egg") == 2:
                winnings,win = Bet*20,True
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

    def textSlot():
        """ The Main function that runs the game loop """
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

def main():
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    window = Tk()
    window.title("Don't Starve Slot Machine")
    window.geometry('640x480+532+0')
    window.minsize(width=640,height=480)
    window.maxsize(width=640,height=480)

    myApp = SlotMachine(window)
    window.mainloop()
    
if __name__ == "__main__": main()
