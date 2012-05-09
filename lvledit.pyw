from __future__ import division, print_function
from math import *
from Tkinter import *
import time
import random

X=1000
Y=900
root = Tk()
canvas = Canvas(root, bg=('#807777'), width=X, height=Y)
canvas.pack()
canvas.focus_force()
root.title("lvl editor za Streljanko zombijev")

mouseX = 0
mouseY = 0
n = 0
keys = []
player_list = []
ovire_list = []
zombij_list = []




class ActiveObject:
    def __init__(self, canvas, seznam, x, y, r):
        self.canvas = canvas
        self.seznam = seznam
        self.x = x
        self.y = y
        self.r = r
        self.type = seznam[0]

class Zombij:
    def __init__(self, canvas, x, y, r):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.color = '#055505'
        self.list = 'zombij_list'
        self.izris()
        
    def kill(self):
        self.canvas.delete(self.index)
        zombij_list.remove(self)
  
    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=self.color, outline="red", width = 0)

        def col_krog(self, ovira):
            if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
                #print("Zaletavam se")
                return True
            return False
        
class Ovira_Krog:
    def __init__(self, canvas, x, y, r):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.color = '#202020'
        self.list = 'ovire_list'
        self.izris()
        
    def kill(self):
        self.canvas.delete(self.index)
        ovire_list.remove(self)
  
    def izris(self):
        try:
            self.kill()
        except:
            pass
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=self.color, outline="red", width = 0)

    def izris_brez(self):
        self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=self.color, outline="red", width = 0)
    
class Player:
    def __init__(self, canvas, x, y, r):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.color = '#450505'
        self.list = 'player_list'
        self.izris()
        
    def kill(self):
        self.canvas.delete(self.index)
        player_list.remove(self)
  
    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=self.color, outline="red", width = 0)

    def izris_brez(self):
        self.canvas.create_oval(self.x - self.r - 20,self.y - self.r - 20,self.x + self.r, self.y + self.r, fill=self.color, outline="red", width = 0)

    def col_krog(self, ovira):
        if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
            #print("Zaletavam se")
            return True
        return False



                





def mousePress(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y

    #if("Mouse1" not in keys):
    #    keys.append("Mouse1")
    print("Miska1")
    activeObject.izris_brez()
    #print(keys)

"""
def mouseRelease(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y

    #if("Mouse1" in keys):
    #    keys.remove("Mouse1")
    print("Miska1 spust")

    #print(keys)
"""

def mouseUpdate(event):
    #print(event.x, event.y)
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    activeObject.x = mouseX
    activeObject.y = mouseY
    activeObject.izris()

def ugasni(event):
    root.destroy()
    root.quit()
    
    
"""
def update_root():
    activeObject.x = mouseX
    activeObject.y = mouseY
    if Mouse1 in keys:
        activeObject.list.append(activeObject)
        activeObject = objects[n](canvas, 20, 20, 10)
    elif 'plus' in keys:
        activeObject.r += 1
    elif 'minus' in keys:
        sctiveObject.r -= 1
    elif up in keys:
        try:
            activeObjectType = objects[n+1]
        except:
            pass
    elif down in keys:
        try:
            activeObjectsType = objects[n-1]
        except:
            pass

    root.after(1, update_root)
"""

canvas.bind("<ButtonPress-1>", mousePress)
canvas.bind("<ButtonRelease-1>", mouseRelease)
canvas.bind("<Motion>", mouseUpdate)
root.bind_all("q", ugasni)
root.bind_all("Q", ugasni)
#


objects = [Ovira_Krog,Player,Zombij]


#activeObject = ActiveObject(canvas, objects, 20, 20, 10)
activeObject = Ovira_Krog(canvas, 100, 100, 10)
activeObject.izris()

#update_root()
#





root.mainloop()
