
# -*- coding: utf-8 -*-

from __future__ import division
from Tkinter import *
import time
import random



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
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill="blue", outline="red", width = 0)

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
        if(vx != 0 and vy != 0):
            self.preveri_premik(self.speed*vx/2**(0.5), self.speed*vy/2**(0.5))
        else:
            self.preveri_premik(self.speed*vx, self.speed*vy)
        self.update()

    def streljaj(self, x, y):
        global metki_list
        metki_list.append(Metek(self.canvas, self.x, self.y, 5, 10, 0, x, y, "black"))
        metki_list[-1].izris()


class Krog:
    def __init__ (self, canvas, x, y, r):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r

    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill="brown", outline="black", width = 2)
    

class Metek:
    def __init__(self, canvas, x, y, r, speed, dmg, destx, desty, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.dmg = dmg
        self.vx =(destx-self.x)
        self.vy =(desty-self.y)
        self.color = color
        
    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, outline="black", width = 0)
    def update(self, t):
        #self.premik(1,1)
        self.premik(self.vx*t, self.vy*t)
        self.canvas.delete(self.index)
        self.izris()
    def premik(self, x, y):
        self.x += x
        self.y += y
    def kill(self):
        self.canvas.delete(self.index)
        metki_list.remove(self)
    #def move(self, x, y, speed):
        
     




            
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
        if('Up' in keys):
            #ply.gor(x - old)
            vy -= tmp
        if 'Down' in keys:
            #ply.dol(x - old)
            vy += tmp
        if 'Left' in keys:
            #ply.levo(x - old)
            vx -= tmp
        if 'Right' in keys:
            #ply.desno(x - old)
            vx += tmp
        #print(vx, vy)
        ply.movement(vx, vy)

    for metek in metki_list:
        metek.update(tmp)
        
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
    print ("clicked at", event.x, event.y)
    ply.streljaj(event.x, event.y)
    



keys = []
player_list = []
ovire_list = []
metki_list = []

nice_blue = "#00A2FF"  
X=800
Y=600
root = Tk()
canvas = Canvas(root, bg="green", width=X, height=Y)
canvas.pack()





############# USTVARI IGRALCA ######################
ply = Player(canvas, 100, 100, 35, 300)
player_list.append(ply)
ply.izris()


############## USTVARI KROG ########################
for i in range (10):
    ovira = Krog(canvas, random.randint(100, 700), random.randint(100, 500), 20)
    ovire_list.append(ovira)
    ovira.izris()


#ply2 = Player(canvas, 100,100,60,500)
#player_list.append(ply2)
#ply2.izris()

canvas.bind("<Button-1>", mouse_input)
root.bind_all("<space>", ply.nastavi(100, 100))
root.bind_all("<Button-3>", destroy)
#root.bind_all("<Key>", key)
root.bind_all("<KeyPress>", keyPressHandler)
root.bind_all("<KeyRelease>", keyReleaseHandler)
#root.bind_all("<Button-1>", updateEvent)
#canvas.bind("<Button-1>", izris)
#canvas.bind("<B1-Motion>", izris)

update(time.time())

#canvas.bind("<Button-1>", xy)
#canvas.bind("<B1-Motion>", addLine)
#canvas.bind("A", delete)

root.mainloop()
