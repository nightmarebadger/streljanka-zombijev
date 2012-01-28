from Tkinter import *

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

    def update(self):
        self.canvas.delete(self.index)
        self.izris()

    def gor(self):
        if ((self.y-self.r)-(self.speed)>= 0):
            self.premik(0, -self.speed)
            self.update()
        else:
            self.premik(0, -(self.y-self.r))
            self.update()

    def dol(self):
        self.premik(0, self.speed)
        self.update()

    def levo(self):
        self.premik(-self.speed, 0)
        self.update()

    def desno(self):
        self.premik(self.speed, 0)
        self.update()

def destroy(event):
    root.destroy()
    
def key(event):
    if event.keysym == 'Up':
        ply.gor()
    if event.keysym == "Down":
        ply.dol()
    if event.keysym == "Left":
        ply.levo()
    if event.keysym == "Right":
        ply.desno()
        
nice_blue = "#00A2FF"  

root = Tk()
canvas = Canvas(root, bg="green", width=800, height=600)
canvas.pack()


ply = Player(canvas, 400, 300, 50, 10)
ply.izris()


root.bind_all("<Button-3>", destroy)
root.bind_all("<Key>", key)
#canvas.bind("<Button-1>", izris)
#canvas.bind("<B1-Motion>", izris)


#canvas.bind("<Button-1>", xy)
#canvas.bind("<B1-Motion>", addLine)
#canvas.bind("A", delete)

root.mainloop()
