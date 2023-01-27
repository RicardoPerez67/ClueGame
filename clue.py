import random

class ClueGame():

    def __init__(self):

        #define your variables and your solution

        self.suspects = ['smoke', 'sledge', 'fuze', 'caviera', 'pulse', 'capitao']

        self.weapons = ['gas grenade','hammer','cluster grenade','knife','fire bolt','C4']

        self.sites = ['cash room', 'basement','kitchen','master bedroom','garage','supply room']

        self.solution = {'Suspect' : random.choice(self.suspects), 'Weapon' : random.choice(self.weapons), 'Site': random.choice(self.sites)}

        #define your players
        
        self.p1 = player()

        self.p2 = player()

        self.turn = True

        self.p1.playername = input ('What is your name player 1?')

        print('good luck ' + self.p1.playername)

        self.p2.playername = input ('What is your name player 2?')

        print('good luck ' + self.p2.playername)
        

        self.currentplayername = ""


        #run until win
        
        self.rununtilwin()
        

    def rununtilwin(self):
        while self.p1.win == False and self.p2.win == False:
            self.checkplayername()
            self.choosemove()
            self.checkplayerfail()
            self.changeplayer()

    def checkplayername(self):
        if self.turn:
            self.currentplayername = self.p1.playername
        else: 
            self.currentplayername = self.p2.playername
        print ('It is ' + self.currentplayername + "'s turn")

    def checkplayerfail(self):
        if self.turn:
            if self.p1.win == False:
                if self.p1.guesses == 0:
                    self.p2.win = True
                    print('great job ' + self.p2.playername + ' you win!')
        else: 
            if self.p2.win == False:
                if self.p2.guesses == 0:
                    self.p1.win = True
                    print('great job ' + self.p1.playername + ' you win!')
        
    
    def winmethod(self):
        print('great job ' + self.currentplayername + ' you win!')

    def changeplayer(self):
        self.turn = not self.turn
        
        #choose your move command

    def choosemove(self):
        print ('Press 1 to investigate a suspect!')
        print ('Press 2 to investigate a weapon!')
        print ('Press 3 to investigate a site!')
        print ('Press 4 to guess!')
        #choose your action
        actionnum = input ('')
        #suspect investigation
        if(actionnum == '1'):
            print('You chose to investigate a suspect')
            print('enter a suspect from the list below')
            print(self.suspects)
            #guess your suspect!
            suspectguess = input ('')
            if (suspectguess == self.solution['Suspect']):
                print('well done ' + self.currentplayername + ' thats the answer!')
            else:
                print('thats not right, better luck next time!')
        if(actionnum == '2'):
            print('You chose to investigate a weapon')
            print('enter a weapon from the list below')
            print(self.weapons)
            #guess your suspect!
            weaponguess = input ('')
            if (weaponguess == self.solution['Weapon']):
                print('well done ' + self.currentplayername + ' thats the answer!')
            else:
                print('thats not right, better luck next time!')
        if(actionnum == '3'):
            print('You chose to investigate a site')
            print('enter a site from the list below')
            print(self.sites)
            #guess your suspect!
            siteguess = input ('')
            if (siteguess == self.solution['Site']):
                print('well done ' + self.currentplayername + ' thats the answer!')
            else:
                print('thats not right, better luck next time!')
        if(actionnum == '4'):
            print('you chose to guess! bold move!')
            if self.turn:
                self.p1.guesses = self.p1.guesses -1
                print('you have')
                print(self.p1.guesses)
                print('guesses')
            else:
                self.p2.guesses = self.p2.guesses -1
                print('you have')
                print(self.p2.guesses)
                print('guesses')
            print('guess a suspect!')
            self.suspectguess2 = input ('')
            print('guess a weapon!')
            self.weaponguess2 = input ('')
            print('guess a site!')
            self.siteguess2 = input ('')
            if self.suspectguess2 == self.solution['Suspect'] and self.weaponguess2 == self.solution['Weapon'] and self.siteguess2 == self.solution['Site']:
                if self.turn:
                    self.p1.win = True
                else:
                    self.p2.win = True
                self.winmethod()
            else: 
                print('good try ' + self.currentplayername + " but you haven't yet solved the mystery!")
                if self.turn:
                    
                    print('you have')
                    print(self.p1.guesses)
                    print('guesses')
                else:
                    
                    print('you have')
                    print(self.p2.guesses)
                    print('guesses')

                

            


    
            




class player():

    def __init__(self):

        self.win = False
        self.guesses = int(3)
        self.playername = ""

game = ClueGame()