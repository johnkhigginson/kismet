'''Kismet'''

'''Dice rolling generator'''

import random
from breezypythongui import EasyFrame
import time
from tkinter import PhotoImage
#from tkinter.font import Font

class DiceGenerator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Kismet")
        
        self.dice = ['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png']
        
        g = '#1B5E20'
        w = '#FFFFFF'
        
        self.setResizable(True)
        self.setSize(600, 600)
        self.setBackground(g)
                           
        self.c1 = self.addButton(text = '   1   ', row = 0, column = 0,
                                 command = self.one)
        self.c1.configure(width = 5, font = 5)
        self.dieone = 0
        
        self.c2 = self.addButton(text = '2', row = 0, column = 1,
                                 command = self.two)
        self.c2.configure(width = 5, font = 5)
        self.dietwo = 0
        
        self.c3 = self.addButton(text = '3', row = 0, column = 2,
                                 command = self.three)
        self.c3.configure(width = 5, font = 5)
        self.diethree = 0
        
        self.c4 = self.addButton(text = '4', row = 0, column = 3,
                                 command = self.four)
        self.c4.configure(width = 5, font = 5)
        self.diefour = 0
        
        self.c5 = self.addButton(text = '5', row = 0, column = 4,
                                 command = self.five)
        self.c5.configure(width = 5, font = 5)
        self.diefive = 0
                       
        self.die1 = self.addLabel(text = '-', row = 1,
                      column = 0, sticky = 'E' + 'W',
                      foreground = g, background = g)
        self.die2 = self.addLabel(text = '-', row = 1,
                      column = 1, sticky = 'E' + 'W',
                      foreground = g, background = g)
        self.die3 = self.addLabel(text = '-', row = 1,
                      column = 2, sticky = 'E' + 'W',
                      foreground = g, background = g)
        self.die4 = self.addLabel(text = '-', row = 1,
                      column = 3, sticky = 'E' + 'W',
                      foreground = g, background = g)
        self.die5 = self.addLabel(text = '-', row = 1,
                      column = 4, sticky = 'E' + 'W',
                      foreground = g, background = g)

        self.image1 = PhotoImage(file = self.dice[5])
        self.image2 = PhotoImage(file = self.dice[5])
        self.image3 = PhotoImage(file = self.dice[5])
        self.image4 = PhotoImage(file = self.dice[5])
        self.image5 = PhotoImage(file = self.dice[5])
        
        self.die1["image"] = self.image1
        self.die2["image"] = self.image2
        self.die3["image"] = self.image3
        self.die4["image"] = self.image4
        self.die5["image"] = self.image5
        
        self.generate = self.addButton(text = 'Roll!', row = 2,
                                       column = 0, columnspan = 2,
                                       command = self.generate)
        self.generate.configure(height = 2, width = 10)
        
        self.tot = self.addLabel(text = "Total:", row = 2, column = 2, sticky = "E",
                                 foreground = '#000000', background = g)
        self.tot.configure(font = 10)
                                 
        self.total = self.addIntegerField(value = 0, row = 2,
                                          column = 3, sticky = "W",
                                          width = 5, state="disabled")
        self.total.configure(font = 10)
        self.generate.configure(width = 10)
        
        '''SCORECARD'''
        self.aceslabel = self.addLabel(text = 'Aces', row = 3, column = 0,
                                       background = w, sticky = 'E',
                                       font = 5)
        self.aceslabel.configure(width = 10)
        
        self.twoslabel = self.addLabel(text = 'Deuces', row = 4, column = 0,
                      background = w, sticky = 'E',
                      font = 3)
        self.twoslabel.configure(width = 10)
        
        self.threeslabel = self.addLabel(text = 'Treys', row = 5, column = 0,
                      background = w, sticky = 'E',
                      font = 3)
        self.threeslabel.configure(width = 10)
        
        self.fourslabel = self.addLabel(text = 'Fours', row = 6, column = 0,
                      background = w, sticky = 'E',
                      font = 3)
        self.fourslabel.configure(width = 10)
        
        self.fiveslabel = self.addLabel(text = 'Fives', row = 7, column = 0,
                      background = w, sticky = 'E',
                      font = 3)
        self.fiveslabel.configure(width = 10)
        
        self.sixeslabel = self.addLabel(text = 'Sixes', row = 8, column = 0,
                      background = w, sticky = 'E',
                      font = 3)
        self.sixeslabel.configure(width = 10)
        
        self.totallabel = self.addLabel(text = 'Total-->', row = 9, column = 0,
                      columnspan = 1, sticky = "E",
                      background = w, font = 5)
        self.totallabel.configure(width = 10)
        
        self.bonuslabel = self.addLabel(text = 'BONUS', row = 10, column = 0,
                      columnspan = 1, background = '#000000',
                      foreground = '#FFFFFF', font = 10,
                      sticky = 'E')
        self.bonuslabel.configure(width = 10)
        
        self.ones = self.addIntegerField(value = 0, row = 3, column = 1,
                                         state = 'disable', sticky = 'W')
        self.ones.configure(width = 3, font = 5)
        
        self.twos = self.addIntegerField(value = 0, row = 4, column = 1,
                                         state = 'disable', sticky = 'W')
        self.twos.configure(width = 3, font = 5)
        
        self.threes = self.addIntegerField(value = 0, row = 5, column = 1,
                                         state = 'disable', sticky = 'W')
        self.threes.configure(width = 3, font = 5)
        
        self.fours = self.addIntegerField(value = 0, row = 6, column = 1,
                                         state = 'disable', sticky = 'W')
        self.fours.configure(width = 3, font = 5)
        
        self.fives = self.addIntegerField(value = 0, row = 7, column = 1,
                                         state = 'disable', sticky = 'W')
        self.fives.configure(width = 3, font = 5)
        
        self.sixes = self.addIntegerField(value = 0, row = 8, column = 1,
                                         state = 'disable', sticky = 'W')
        self.sixes.configure(width = 3, font = 5)
        
        self.totalscore = self.addIntegerField(value = 0, row = 9, column = 1,
                                         state = 'disable', sticky = 'W')
        self.totalscore.configure(width = 3, font = 5)
        
        self.bonus = self.addIntegerField(value = 0, row = 10, column = 1,
                                         state = 'disable', sticky = 'W')
        self.bonus.configure(width = 3, font = 5)
        
    def generate(self):
        
        dielist = [self.dieone, self.dietwo, self.diethree, self.diefour, self.diefive]
        imagelist = [self.image1, self.image2, self.image3, self.image4, self.image5]
        
        for i in range(10):
            x1 = random.randint(0, 5)
            y1 = random.randint(0, 5)
            z1 = random.randint(0, 5)
            a1 = random.randint(0, 5)
            b1 = random.randint(0, 5)
            
#            shakelist = [x1, y1, z1, a1, b1]
            
#            for i in range(5):
#                if dielist[i] == 0:
#                    imagelist[i].configure(file = self.dice[shakelist[i]])
#                    time.sleep(.05)
#                    self.update()
            
            if self.dieone == 0:
                self.image1.configure(file = self.dice[x1])
            if self.dietwo == 0:
                self.image2.configure(file = self.dice[y1])
            if self.diethree == 0:
                self.image3.configure(file = self.dice[z1])
            if self.diefour == 0:
                self.image4.configure(file = self.dice[a1])
            if self.diefive == 0:
                self.image5.configure(file = self.dice[b1])
                
            time.sleep(.02)
            self.update()
        
        
        if self.dieone == 0:
            self.x = random.randint(0, 5)
        if self.dietwo == 0:
            self.y = random.randint(0, 5)
        if self.diethree == 0:
            self.z = random.randint(0, 5)
        if self.diefour == 0:
            self.a = random.randint(0, 5)
        if self.diefive == 0:
            self.b = random.randint(0, 5)
        
        lyst = [self.x, self.y, self.z, self.a, self.b]
        
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        
        for i in lyst:
            if i == 0:
                ones += 1
            elif i == 1:
                twos += 2
            elif i == 2:
                threes += 3
            elif i == 3:
                fours += 4
            elif i == 4:
                fives += 5
            elif i == 5:
                sixes += 6
                
        self.ones.setValue(ones)
        self.twos.setValue(twos)
        self.threes.setValue(threes)
        self.fours.setValue(fours)
        self.fives.setValue(fives)
        self.sixes.setValue(sixes)
        
        for i in range(5):
            if dielist[i] == 0:
                imagelist[i].configure(file = self.dice[lyst[i]])
                lyst[i] = lyst[i] + 1
            elif self.dieone > 0:
                lyst[i] = 0
            
        tot = 0
        for i in lyst:
            tot += i
        
        self.total.setValue(tot)
    
    def one(self):
        if self.dieone == 0:
            self.dieone += 1
            self.die1.configure(state = "disable")
        elif self.dieone > 0:
            self.dieone = 0
            self.die1.configure(state = "normal")

    def two(self):
        if self.dietwo == 0:
            self.dietwo += 1
            self.die2.configure(state = "disable")
        elif self.dietwo > 0:
            self.dietwo = 0
            self.die2.configure(state = "normal")
            
    def three(self):
        if self.diethree == 0:
            self.diethree += 1
            self.die3.configure(state = "disable")
        elif self.diethree > 0:
            self.diethree = 0
            self.die3.configure(state = "normal")
            
    def four(self):
        if self.diefour == 0:
            self.diefour += 1
            self.die4.configure(state = "disable")
        elif self.diefour > 0:
            self.diefour = 0
            self.die4.configure(state = "normal")
            
    def five(self):
        if self.diefive == 0:
            self.diefive += 1
            self.die5.configure(state = "disable")
        elif self.diefive > 0:
            self.diefive = 0
            self.die5.configure(state = "normal")
            
            
    

def main():
    DiceGenerator().mainloop()

if __name__ == '__main__':
    main()