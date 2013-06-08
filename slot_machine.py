# Source File Name: slot_machine.py
# Author's Name: Chris Bentley
# Last Modified By: Chris Bentley
# Date Last Modified: June 07, 2013
""" 
    PROGRAM DESCRIPTION: It is a Python program that takes a users bet as input and given
                        a random output based on probability, the end result will most likely end
                        in the user running out of money to bet.
                        
    VERSION 0.5: The Big Info Update
                    - Added Labels to Display when the player wins a Jackpot
                    - Added a small label to display the change in cash after each spin
                    - Minor move of the buttons to accomodate labels
                    - Some minor documentation changes
                    - Added a Retry/Quit Button. Quit does not like being local for some reason.
                    - Game acknowledges you have less money than a betting button!

    
"""

# import statements
import random
import ttk
from Tkinter import *
from PIL import Image, ImageTk

class SlotMachine:
    
    def __init__(self, master=None):

        self.buttonFont = "-family Forte -size 22 -weight normal -slant roman -underline 0 -overstrike 0"
        self.displayFont = "-family Forte -size 18 -weight normal -slant roman -underline 0 -overstrike 0"
        self.winningFont = "-family Forte -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
        
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

        #Import Slot Images
        self.berries_img = Image.open("images/berries.png")
        self.berries_imgTk = ImageTk.PhotoImage(self.berries_img)

        self.rot_img = Image.open("images/rot.png")
        self.rot_imgTk = ImageTk.PhotoImage(self.rot_img)

        self.seeds_img = Image.open("images/seeds.png")
        self.seeds_imgTk = ImageTk.PhotoImage(self.seeds_img)

        self.durian_img = Image.open("images/durian.png")
        self.durian_imgTk = ImageTk.PhotoImage(self.durian_img)

        self.carrot_img = Image.open("images/carrot.png")
        self.carrot_imgTk = ImageTk.PhotoImage(self.carrot_img)

        self.fruit_img = Image.open("images/fruit.png")
        self.fruit_imgTk = ImageTk.PhotoImage(self.fruit_img)

        self.egg_img = Image.open("images/egg.png")
        self.egg_imgTk = ImageTk.PhotoImage(self.egg_img)

        self.ham_img = Image.open("images/ham.png")
        self.ham_imgTk = ImageTk.PhotoImage(self.ham_img)

        self.waffles_img = Image.open("images/waffles.png")
        self.waffles_imgTk = ImageTk.PhotoImage(self.waffles_img)

        self.taffy_img = Image.open("images/taffy.png")
        self.taffy_imgTk = ImageTk.PhotoImage(self.taffy_img)

        self.quitButton_img = Image.open("images/quit.png")
        self.quitButton_imgTk = ImageTk.PhotoImage(self.quitButton_img)

        self.retryButton_img = Image.open("images/retry.png")
        self.retryButton_imgTk = ImageTk.PhotoImage(self.retryButton_img)

        #Display Bet Amount
        self.betAmount = Label (self.bg_panel)
        self.betAmount.place(x=420,y=310,height=35,width=150)
        self.betAmount.configure(background="#000000")
        self.betAmount.configure(borderwidth="0")
        self.betAmount.configure(font=self.buttonFont)
        self.betAmount.configure(foreground="#ff0000")
        self.betAmount.configure(anchor="n")
        self.betAmount.configure(text="0000")

        #Display Bet Label
        self.betLabel = Label (self.bg_panel)
        self.betLabel.place(x=320, y=310, height=35, width=50)
        self.betLabel.configure(background="#000000")
        self.betLabel.configure(borderwidth="0")
        self.betLabel.configure(font=self.buttonFont)
        self.betLabel.configure(foreground="#ff0000")
        self.betLabel.configure(anchor="n")
        self.betLabel.configure(text="Bet:")

        #Display Money Amount
        self.cashAmount = Label (self.bg_panel)
        self.cashAmount.place(x=170,y=310,height=35,width=150)
        self.cashAmount.configure(background="#000000")
        self.cashAmount.configure(borderwidth="0")
        self.cashAmount.configure(font=self.buttonFont)
        self.cashAmount.configure(foreground="#ff0000")
        self.cashAmount.configure(anchor="n")
        self.cashAmount.configure(text="1000")

        #Display Money Label
        self.cashLabel = Label (self.bg_panel)
        self.cashLabel.place(x=60, y=310, height=35, width=100)
        self.cashLabel.configure(background="#000000")
        self.cashLabel.configure(borderwidth="0")
        self.cashLabel.configure(font=self.buttonFont)
        self.cashLabel.configure(foreground="#ff0000")
        self.cashLabel.configure(anchor="n")
        self.cashLabel.configure(text="Cash:")

        #Configure the Display Label
        self.displayLabel = Label (self.bg_panel)
        self.displayLabel.place(x=125, y=250, height=35, width=400)
        self.displayLabel.configure(background="#000000")
        self.displayLabel.configure(borderwidth="0")
        self.displayLabel.configure(font=self.displayFont)
        self.displayLabel.configure(foreground="#ffffff")
        self.displayLabel.configure(anchor="n")

        #Configure the Winnings Label
        self.winLabel = Label (self.bg_panel)
        self.winLabel.place(x=195, y=340, height=20, width=100)
        self.winLabel.configure(background="#000000")
        self.winLabel.configure(borderwidth="0")
        self.winLabel.configure(font=self.winningFont)
        self.winLabel.configure(foreground="#ffffff")
        self.winLabel.configure(anchor="n")

        #Display Jackpot Amount
        self.jackpotAmount = Label (self.bg_panel)
        self.jackpotAmount.place(x=360,y=90,height=35,width=150)
        self.jackpotAmount.configure(background="#000000")
        self.jackpotAmount.configure(borderwidth="0")
        self.jackpotAmount.configure(font=self.buttonFont)
        self.jackpotAmount.configure(foreground="#ff0000")
        self.jackpotAmount.configure(anchor="n")
        self.jackpotAmount.configure(text="1000")

        #Display Jackpot Label
        self.jackpotLabel = Label (self.bg_panel)
        self.jackpotLabel.place(x=150, y=90, height=35, width=150)
        self.jackpotLabel.configure(background="#000000")
        self.jackpotLabel.configure(borderwidth="0")
        self.jackpotLabel.configure(font=self.buttonFont)
        self.jackpotLabel.configure(foreground="#ff0000")
        self.jackpotLabel.configure(anchor="n")
        self.jackpotLabel.configure(text="Jackpot:")

        # Display the Quit
        self.quitButton = Button(self.bg_panel)
        self.quitButton.place(x=588, y=428, height=50, width=50)
        self.quitButton.configure(borderwidth="0")
        self.quitButton.configure(image=self.quitButton_imgTk)
        self.quitButton.configure(cursor="hand2")
        self.quitButton.configure(background="black")
        self.quitButton.bind("<Button-1>", lambda event: window.destroy())

        # Display the Retry button
        self.retryButton = Button(self.bg_panel)
        self.retryButton.place(x=2, y=428, height=50, width=50)
        self.retryButton.configure(borderwidth="0")
        self.retryButton.configure(image=self.retryButton_imgTk)
        self.retryButton.configure(cursor="hand2")
        self.retryButton.configure(background="black")
        self.retryButton.bind("<Button-1>",self.retry)

        # Display the Bet 1000 button
        self.bet1000Button = Button(self.bg_panel)
        self.bet1000Button.place(x=425, y=400, height=46, width=125)
        self.bet1000Button.configure(borderwidth="0")
        self.bet1000Button_img = PhotoImage(file="images/button.gif")
        self.bet1000Button.configure(image=self.bet1000Button_img)
        self.bet1000Button.configure(cursor="hand2")
        self.bet1000Button.configure(font=self.buttonFont, compound="center", text="Bet 1000")
        self.bet1000Button.bind("<Button-1>",self.bet1000)

        # Display the Bet 100 button
        self.bet100Button = Button(self.bg_panel)
        self.bet100Button.place(x=300, y=350, height=46, width=125)
        self.bet100Button.configure(borderwidth="0")
        self.bet100Button_img = PhotoImage(file="images/button.gif")
        self.bet100Button.configure(image=self.bet100Button_img)
        self.bet100Button.configure(cursor="hand2")
        self.bet100Button.configure(font=self.buttonFont, compound="center", text="Bet 100")
        self.bet100Button.bind("<Button-1>",self.bet100)

        # Display the Bet 250 button
        self.bet250Button = Button(self.bg_panel)
        self.bet250Button.place(x=425, y=350, height=46, width=125)
        self.bet250Button.configure(borderwidth="0")
        self.bet250Button_img = PhotoImage(file="images/button.gif")
        self.bet250Button.configure(image=self.bet250Button_img)
        self.bet250Button.configure(cursor="hand2")
        self.bet250Button.configure(font=self.buttonFont, compound="center", text="Bet 250")
        self.bet250Button.bind("<Button-1>",self.bet250)

        # Display the Bet 500 button
        self.bet500Button = Button(self.bg_panel)
        self.bet500Button.place(x=300, y=400, height=46, width=125)
        self.bet500Button.configure(borderwidth="0")
        self.bet500Button_img = PhotoImage(file="images/button.gif")
        self.bet500Button.configure(image=self.bet500Button_img)
        self.bet500Button.configure(cursor="hand2")
        self.bet500Button.configure(font=self.buttonFont, compound="center", text="Bet 500")
        self.bet500Button.bind("<Button-1>",self.bet500)

        # Display the Spin button
        self.spinButton = Button(self.bg_panel)
        self.spinButton.place(x=120, y=375, height=46, width=125)
        self.spinButton.configure(borderwidth="0")
        self.spinButton_img = PhotoImage(file="images/button.gif")
        self.spinButton.configure(image=self.spinButton_img)
        self.spinButton.configure(cursor="hand2")
        self.spinButton.configure(font=self.buttonFont, compound="center", text="Spin")
        self.spinButton.bind("<Button-1>",self.spinReels)

    def bet100(self, event):
        if int(self.cashAmount["text"]) >= 100:
            self.betAmount["text"] = 100
        
    def bet250(self, event):
        if int(self.cashAmount["text"]) >= 250:
            self.betAmount["text"] = 250

    def bet500(self, event):
        if int(self.cashAmount["text"]) >= 500:
            self.betAmount["text"] = 500

    def bet1000(self, event):
        if int(self.cashAmount["text"]) >= 1000:
            self.betAmount["text"] = 1000

    def retry(self, event):
        self.cashAmount["text"] = 1000
        self.betAmount["text"] = "0000"
        self.displayLabel.configure(text="")
        self.winLabel.configure(text="")

        self.bg_panel.delete(ALL)
        # Display the Slot Machine Image on a Canvas Panel
        self.bg_panel.create_image(0, 0, image = self.bg_imgTk, anchor = NW)

        #Display the Reel Slot
        self.bg_panel.create_image(200, 150, image = self.reel1_imgTk, anchor = NW)

        #Display the Reel Slot
        self.bg_panel.create_image(290, 150, image = self.reel2_imgTk, anchor = NW)

        #Display the Reel Slot
        self.bg_panel.create_image(380, 150, image = self.reel3_imgTk, anchor = NW)

        self.bet100Button.configure(state=NORMAL)
        self.bet250Button.configure(state=NORMAL)
        self.bet500Button.configure(state=NORMAL)
        self.bet1000Button.configure(state=NORMAL)

    def spinReels(self, event):
        Cash = int(self.cashAmount["text"])
        Bet = int(self.betAmount["text"])
        Jackpot = int(self.jackpotAmount["text"])
        BetOk = False
    
        if Bet > Cash:
            BetOk = False
        else:
            BetOk = True

        if Cash >= 100 and Bet > 0 and BetOk == True:
            # [0]Fruit, [1]Fruit, [2]Fruit
            Bet_Line = [" "," "," "]
            Outcome = [0,0,0]
            food = self.rot_imgTk
            winnings = 0
            win = False

            Cash -= Bet
            Jackpot += (Bet/5)

            self.bg_panel.delete(ALL)
            # Display the Slot Machine Image on a Canvas Panel
            self.bg_panel.create_image(0, 0, image = self.bg_imgTk, anchor = NW)

            #Display the Reel Slot
            self.bg_panel.create_image(200, 150, image = self.reel1_imgTk, anchor = NW)

            #Display the Reel Slot
            self.bg_panel.create_image(290, 150, image = self.reel2_imgTk, anchor = NW)

            #Display the Reel Slot
            self.bg_panel.create_image(380, 150, image = self.reel3_imgTk, anchor = NW)
            
            # Spin those reels
            for spin in range(3):
                Outcome[spin] = random.randrange(1,64,1)
                # Spin those Reels!
                if Outcome[spin] >= 1 and Outcome[spin] <=18:   # 28.13% Chance
                    Bet_Line[spin] = "Rot"
                    food = self.rot_imgTk
                if Outcome[spin] >= 19 and Outcome[spin] <=28:  # 15.62% Chance
                    Bet_Line[spin] = "Durian"
                    food = self.durian_imgTk
                if Outcome[spin] >= 29 and Outcome[spin] <=36:  # 12.50% Chance
                    Bet_Line[spin] = "Seeds"
                    food = self.seeds_imgTk
                if Outcome[spin] >= 37 and Outcome[spin] <=43:  # 10.94% Chance
                    Bet_Line[spin] = "Berries"
                    food = self.berries_imgTk
                if Outcome[spin] >= 44 and Outcome[spin] <=49:  # 9.37%  Chance
                    Bet_Line[spin] = "Carrot"
                    food = self.carrot_imgTk
                if Outcome[spin] >= 50 and Outcome[spin] <=54:  # 7.81%  Chance
                    Bet_Line[spin] = "Dragon Fruit"
                    food = self.fruit_imgTk
                if Outcome[spin] >= 55 and Outcome[spin] <=58:  # 6.25%  Chance
                    Bet_Line[spin] = "Cooked Egg"
                    food = self.egg_imgTk
                if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 4.69%  Chance
                    Bet_Line[spin] = "Honey Ham"
                    food = self.ham_imgTk
                if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.13%  Chance
                    Bet_Line[spin] = "Waffles"
                    food = self.waffles_imgTk
                if Outcome[spin] == 64:                         # 1.56%  Chance
                    Bet_Line[spin] = "Taffy"
                    food = self.taffy_imgTk

                if spin == 0:
                    slot1 = self.bg_panel.create_image(202, 150, image = food, anchor = NW)
                elif spin == 1:
                    slot2 = self.bg_panel.create_image(292, 150, image = food, anchor = NW)
                elif spin == 2:
                    slot3 = self.bg_panel.create_image(382, 150, image = food, anchor = NW)      
        

            Food_Reel = Bet_Line

            if Food_Reel.count("Durian") == 3:
                winnings,win = Bet*3,True
            elif Food_Reel.count("Seeds") == 3:
                winnings,win = Bet*6,True
            elif Food_Reel.count("Berries") == 3:
                winnings,win = Bet*10,True
            elif Food_Reel.count("Carrot") == 3:
                winnings,win = Bet*15,True
            elif Food_Reel.count("Dragon Fruit") == 3:
                winnings,win = Bet*25,True
            elif Food_Reel.count("Cooked Egg") == 3:
                winnings,win = Bet*50,True
            elif Food_Reel.count("Honey Ham") == 3:
                winnings,win = Bet*100,True
            elif Food_Reel.count("Waffles") == 3:
                winnings,win = Bet*200,True
            elif Food_Reel.count("Taffy") == 3:
                winnings,win = Bet*500,True
            
            # Match 2
            elif Food_Reel.count("Rot") == 0:
                if Food_Reel.count("Durian") == 2:
                    winnings,win = Bet*1,True
                if Food_Reel.count("Seeds") == 2:
                    winnings,win = Bet*2,True
                elif Food_Reel.count("Berries") == 2:
                    winnings,win = Bet*3,True
                elif Food_Reel.count("Carrot") == 2:
                    winnings,win = Bet*5,True
                elif Food_Reel.count("Dragon Fruit") == 2:
                    winnings,win = Bet*10,True
                elif Food_Reel.count("Cooked Egg") == 2:
                    winnings,win = Bet*20,True
                elif Food_Reel.count("Honey Ham") == 2:
                    winnings,win = Bet*30,True
                elif Food_Reel.count("Waffles") == 2:
                    winnings,win = Bet*50,True
                elif Food_Reel.count("Taffy") == 2:
                    winnings,win = Bet*100,True
            
                # Match TAFFY!
                elif Food_Reel.count("Taffy") == 1:
                    winnings, win = Bet*5,True
                    
                else:
                    winnings, win = Bet,True

            cashText = ""

            if win:    
                Cash += winnings
            
                # Jackpot 1 in 450 chance of winning
                jackpot_try = random.randrange(1,51,1)
                jackpot_win = random.randrange(1,51,1)
                if  jackpot_try  == jackpot_win:
                    Cash += Jackpot
                    cashText = "+" + str(winnings - Bet + Jackpot)
                    displayText = "You won the Jackpot! Here's $" + str(Jackpot)
                    Jackpot = 1000
                    self.displayLabel.configure(text=displayText)
                    
                elif jackpot_try != jackpot_win:
                    displayText = ""
                    self.displayLabel.configure(text=displayText)
                    cashText = "+" + str(winnings - Bet)

                
            else:
                cashText = "-" + str(Bet)
                displayText = ""
                self.displayLabel.configure(text=displayText)

            self.winLabel.configure(text=cashText)
                

        self.cashAmount["text"] = Cash
        self.jackpotAmount["text"] = Jackpot

        if Bet > Cash or Bet == 0:
            self.betAmount["text"] = "0000"
        else:
            self.betAmount["text"] = Bet

        if Cash < 100:
            self.bet100Button.configure(state=DISABLED)
        if Cash < 250:
            self.bet250Button.configure(state=DISABLED)
        if Cash < 500:
            self.bet500Button.configure(state=DISABLED)
        if Cash < 1000:
            self.bet1000Button.configure(state=DISABLED)

        if Cash >= 100:
            self.bet100Button.configure(state=NORMAL)
        if Cash >= 250:
            self.bet250Button.configure(state=NORMAL)
        if Cash >= 500:
            self.bet500Button.configure(state=NORMAL)
        if Cash >= 1000:
            self.bet1000Button.configure(state=NORMAL)

window = Tk()

def main():
    window.title("Don't Starve Slot Machine")
    window.geometry('640x480+532+0')
    window.minsize(width=640,height=480)
    window.maxsize(width=640,height=480)

    mySlotMachine = SlotMachine(window)
    window.mainloop()
    
if __name__ == "__main__": main()
