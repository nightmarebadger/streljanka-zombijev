# -*- coding: utf-8 -*-

from __future__ import division
from Tkinter import *
import time
import random

"""
ovire_list -> ovire_krog_list
Krog -> Ovira_Krog
"""


lastx = 0
lasty = 0

class App:
    def __init__(self, root):
        fm = Frame(root, width = 500, height = 500, bg = "red")
        fm.pack(side = TOP, expand = NO, fill = NONE)


def xy(event):
    global lastx, lasty
    lastx = event.x
    lasty = event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx = event.x
    lasty = event.y

def delete(event):
    canvas.delete("all")

############################################################################
########################## PLAYER ##########################################
############################################################################

class Player:
    def __init__ (self, canvas, x, y, r, speed):
        self.speed = speed
        self.canvas = canvas
        self.r = r
        self.x = x
        self.y = y

    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=('#450505'), outline="red", width = 0)

    def premik(self, x, y):
        self.x += x
        self.y += y

    def nastavi(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.canvas.delete(self.index)
        self.izris()

    def neki(self):
        player_list.remove(self)


    def col_krog(self, ovira):
        if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
            #print("Zaletavam se")
            return True
        return False

    def preveri_premik(self, x, y):
        if(x == 0 and y == 0):
            return False
        self.premik(x, y)
        if ((self.y-self.r) < 0):
            self.premik(-x, -y)
            return False
        if ((self.y+self.r) >=Y):
            self.premik(-x, -y)
            return False
        if ((self.x+self.r) >= X):
            self.premik(-x, -y)
            return False
        if ((self.x-self.r) < 0):
            self.premik(-x, -y)
            return False

        for ovira in ovire_list:
            if(self.col_krog(ovira) == True):
                self.premik(-x, -y)
                return False

        return True

    def movement(self, vx, vy):
        if(vx == 0 and vy == 0):
            return False
        if(vx != 0 and vy != 0):
            self.preveri_premik(self.speed*vx/2**(0.5), self.speed*vy/2**(0.5))
        else:
            self.preveri_premik(self.speed*vx, self.speed*vy)
        self.update()

    def streljaj(self, x, y):
        global metki_list
        metki_list.append(Metek(self.canvas, self.x, self.y, 5, 350, 10, x, y, "black"))
        metki_list[-1].izris()

#########################################################################################################################  tukaj je to ################
'''
class Weapon:
    def __init__(self, dmg, rof, rng, x, y):
        self.dmg = dmg
        self.rof = rof
        self.range = rng
    def streljaj(self):
'''
##########################################################

class Ovira_Krog:
    def __init__ (self, canvas, x, y, r):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r

    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=('#202020'))

###########################################################    

class Metek:
    def __init__(self, canvas, x, y, r, speed, dmg, destx, desty, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.dmg = dmg
        self.color = color

        
        tx = abs(self.x - destx)
        ty = abs(self.y - desty)
        try:
            self.vx = -(tx/(self.x-destx))*tx/((tx**2+ty**2)**(1/2))
            self.vy = -(ty/(self.y-desty))*ty/((tx**2+ty**2)**(1/2))
        except ZeroDivisionError:
            print('ustrelil si tocno v sredino samega sebe')
            self.vx =0
            self.vy =0

        #print(self.vx, self.vy, abs(self.vx+self.vy))
        
        
        
        
    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, outline="black", width = 0)
    def update(self, t):
        #print("Update!")
        #self.premik(1,1)
        self.premik(self.vx*t*self.speed, self.vy*t*self.speed)
        if (self.zunaj() == False and self.zadeni() == False and self.zombij() == False):
            self.canvas.delete(self.index)
            self.izris()
       
    def premik(self, x, y):
        self.x += x
        self.y += y
        
    def kill(self):
        self.canvas.delete(self.index)
        metki_list.remove(self)

    def col_krog(self, ovira):
        if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
            #print("Zaletavam se")
            return True
        return False
    def zadeni(self):
        for ovira in ovire_list:
            if(self.col_krog(ovira) == True):
                self.kill()
                return True
        return False

    def zombij(self):
        for zombij in zombij_list:
            #print("Yo")
            if(self.col_krog(zombij) == True):
                self.kill()
                zombij.ranjen(self.dmg)
                return True
        return False
    
    def zunaj(self):
        if ((self.x+self.r)<0 or (self.x-self.r)>X):
            self.kill()
            return True
        elif((self.y+self.r)<0 or (self.y-self.r)>Y):
            self.kill()
            return True
        else:
            return False
    #def move(self, x, y, speed):
        
#############################################################################################################################
'''
class HpBar:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def izris_frame(self,zombijx, zombijy, zombijr):
        self = self.canvas.create_rectangle(zombijx-(zombijr*0.9), zombijy-(zombijr+15), zombijx+(zombijr*0.9), zombijy-(zombijr+5), outline = 'black', width = 2)

    def kill(self):
        #print('to se zgodi')
        self.canvas.delete(self.index)
############################################
    def hpbar_refresh(self):
        if self.hpbar_create == True:
                self.hpbar_kill()
                self.hpbar_izris()
        else:
            self.hpbar_create()
    def hpbar_create(self):
        hpbar_list.append
        return True
    def hpbar_izris(self):
        self = self.canvas.create_rectangle(self.x-(self.r*0.9), self.y-(self.r+15), self.x+(self.r*0.9), self.y-(self.r+5), outline = 'black', width = 2)
    def hpbar_kill(self):
        self.canvas.remove(self.index)
        hpbar_list.remove(self)
    ##############################################

    def hpbar_create(self):
        hpbar_list.append(HpBar(canvas))

    def hpbar_refresh(self):
        try:
            self.hpbar.kill()
            self.hpbar.izris_frame(self.x, self.y, self.r)
            print ('izrise')
        except AttributeError:
            pass

    '''
    
#????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        
class Zombij:
    def __init__(self, canvas, x, y, r, speed, health, dmg,):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.health = health
        self.dmg = dmg
        self.vx = 0
        self.vy = 0
        
        

    #def update_hpbar(self):
        #hpbar.izris_frame(int(-self.r*1.5),

    def update(self, t):
        self.update_dest()
        if(self.preveri_premik(self.vx*t*self.speed, self.vy*t*self.speed) == True):
            self.canvas.delete(self.index)
            self.izris()
             

    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill= ('#055505'), outline="black", width = 1)



        

    def ranjen(self, hp):
        self.health -= hp
        if(self.health <= 0):
            print("Kill")
            self.kill()
            
    def preveri_zivljenje(self):
        if(self.health() <= 0):
            self.kill()

    def kill(self):
        self.canvas.delete(self.index)
        zombij_list.remove(self)

    def premik(self, x, y):
        self.x += x
        self.y += y

    def zbudi_metek(self):
        for metek in metki_list:
            if ((((self.x-metek.x)**2+(self.y-metek.y)**2)**0.5)<300):
                return True

    def update_dest(self):
        if (((((self.x-ply.x)**2+(self.y-ply.y)**2)**0.5)<300)or(self.zbudi_metek()==True)):
            try:
                tx = abs(self.x - ply.x)
                ty = abs(self.y - ply.y)
                self.vx = -(tx/(self.x-ply.x))*tx/((tx**2+ty**2)**(1/2))
                self.vy = -(ty/(self.y-ply.y))*ty/((tx**2+ty**2)**(1/2))
            except ZeroDivisionError:
                pass
        else:
            self.vx = 0
            self.vy = 0

        #print(self.vx, self.vy)

    

    def col_krog(self, ovira):
        if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
            #print("Zaletavam se")
            return True
        return False

    def preveri_premik(self, x, y):
        if(x == 0 and y == 0):
            return False
        self.premik(x, y)
        if ((self.y-self.r) < 0):
            self.premik(-x, -y)
            return False
        if ((self.y+self.r) >=Y):
            self.premik(-x, -y)
            return False
        if ((self.x+self.r) >= X):
            self.premik(-x, -y)
            return False
        if ((self.x-self.r) < 0):
            self.premik(-x, -y)
            return False

        for ovira in ovire_list:
            if(self.col_krog(ovira) == True):
                self.premik(-x, -y)
                return False

        return True
  
        


            
def destroy(event):
    root.destroy()
#star nacin premikanja
'''    
def key(event):
    if event.keysym == 'Up':
        ply.gor()
    if event.keysym == "Down":
        ply.dol()
    if event.keysym == "Left":
        ply.levo()
    if event.keysym == "Right":
        ply.desno()
'''
#####################

def updateEvent(event):
    update(time.time())


def update(old):
    t = time.time()
    tmp = t - old
    vx = 0
    vy = 0
    for ply in player_list:
        if 'w' in keys or 'Up' in keys:
            #ply.gor(x - old)
            vy -= tmp
        if 's' in keys or 'Down' in keys:
            #ply.dol(x - old)
            vy += tmp
        if 'a' in keys or 'Left' in keys:
            #ply.levo(x - old)
            vx -= tmp
        if 'd' in keys or 'Right' in keys:
            #ply.desno(x - old)
            vx += tmp
        #print(vx, vy)
        if(vx != 0 or vy != 0):
            ply.movement(vx, vy)

    for metek in metki_list:
        metek.update(tmp)

    for zombij in zombij_list:
        zombij.update(tmp)
        
    root.after(1, update, t)

def keyPressHandler(event):
    if(event.keysym not in keys):
        keys.append(event.keysym)
    
def keyReleaseHandler(event):
    if(event.keysym in keys):
        keys.remove(event.keysym)

#####################################
"""
mouse_x=0
mouse_y=0
mouse
"""

def mouse_input(event):
#    print ("clicked at", event.x, event.y)
    ply.streljaj(event.x, event.y)
    


hpbar_list = []
keys = []
player_list = []
ovire_list = []
zombij_list = []
metki_list = []

nice_blue = "#00A2FF"  
X=1000
Y=900
root = Tk()
canvas = Canvas(root, bg=('#807777'), width=X, height=Y)
canvas.pack()




############# USTVARI IGRALCA ######################
ply = Player(canvas, 100, 100, 35, 300)
player_list.append(ply)
ply.izris()




#===============postavi okrogle ovire========================#

for i in range (10):
    ovira = Ovira_Krog(canvas, random.randint(150, X-100), random.randint(150, Y-100), random.randint(10, 50))
    ovire_list.append(ovira)
    ovira.izris()

#===============ustvari zombije==============================#

#self, canvas, x, y, r, speed, health, dmg)

for i in range(20):
    r = random.randint(10,50)
    zombij_list.append(Zombij(canvas, random.randint(r, X-r), random.randint(r, Y-r), r, random.randint(10,250), 20, 10))
    zombij_list[-1].izris()

def spawn_zombij(event):
    r = random.randint(10,50)
    zombij_list.append(Zombij(canvas, random.randint(r, X-r), random.randint(r, Y-r), r, random.randint(10,250), 20, 10))
    zombij_list[-1].izris()


"""
zombij = Zombij(canvas, 600, 400, 40, 100, 20, 0)
zombij_list.append(zombij)
zombij.izris()

zombij = Zombij(canvas, 300, 200, 40, 0, 20, 0)
zombij_list.append(zombij)
zombij.izris()
"""

#!!!!!!!!!!!!! RANDOM LEVEL !!!!!!!!!!!!!!!!!!!!!!!#


#================GLOBALNE TIPKE======================#
canvas.bind("<Button-1>", mouse_input)
root.bind_all("<space>", spawn_zombij)
root.bind_all("<Button-3>", destroy)
root.bind_all("<KeyPress>", keyPressHandler)
root.bind_all("<KeyRelease>", keyReleaseHandler)


update(time.time())

#canvas.bind("<Button-1>", xy)
#canvas.bind("<B1-Motion>", addLine)
#canvas.bind("A", delete)

root.mainloop()

