# -*- coding: utf-8 -*-

from __future__ import division, print_function
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
    class HpBar:
        def __init__(self, canvas, player):
            self.canvas = canvas
            self.player = player
        
        def izris_frame(self):
            self.frame_index = self.canvas.create_rectangle(100, Y-25, X-100, Y-10, outline = 'black', width = 2)
        def izris_hpbar(self):
            if(self.player.hp > 0):
                self.hpbar_index = self.canvas.create_rectangle(101, Y-24, (X-101)*(self.player.hp/self.player.maxhp), Y-11, fill="red", width=0)
     

        def izris(self):
            self.izris_frame()
            self.izris_hpbar()

        def kill(self):
            self.canvas.delete(self.frame_index)
            self.canvas.delete(self.hpbar_index)
        
        def update(self):
            self.kill()
            self.izris()

            
    
    def __init__ (self, canvas, x, y, r, speed, hp, maxhp):
        self.speed = speed
        self.canvas = canvas
        self.r = r
        self.x = x
        self.y = y
        self.hp = hp
        self.maxhp = maxhp
        self.hpBar = self.HpBar(self.canvas, self)
        self.hpBar.izris()
        self.basic_color = '#450505'
        self.color = '#450505'
        self.col_color = '#fffffe'
        self.reloading = False
        self.rldbar = rldBar(self.canvas, self)
        

    def weaponInit(self, wpn):
        self.weapon = wpn
        self.weapon.canvas = self.canvas
        self.weapon.player = self
    
    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r,self.y - self.r,self.x + self.r, self.y + self.r, fill=self.color, outline="red", width = 0)

    def premik(self, x, y):
        self.x += x
        self.y += y

    def nastavi(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if(('r' in keys) and (not self.reloading)):
            if(self.weapon.rld_t == None):
                self.weapon.rld_t = time.time()
                self.reloading = True
        if(self.reloading == True):
            self.weapon.rld()
            self.rldbar.update()
        
        self.col_zombij()
        self.canvas.delete(self.index)
        self.izris()
        #print(self.hp)
        
    def col_zombij(self):
        for ovira in zombij_list:
            if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
                #print("Zaletavam se")
                self.color = self.col_color
                break
            else:
                self.color = self.basic_color
   

    def col_krog(self, ovira):
        if(((self.x-ovira.x)**2 + (self.y-ovira.y)**2)**0.5 < self.r + ovira.r):
            #print("Zaletavam se")
            return True
        return False

    def ranjen(self, dmg):
        self.hp -= dmg
        
    '''
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
'''
    def preveri_premik(self, x, y):
        self.premik(x, y)
        if ((self.y-self.r) < 0):
            self.premik(0, -y)
            return False
        if ((self.y+self.r) >=Y):
            self.premik(0, -y)
            return False
        if ((self.x+self.r) >= X):
            self.premik(-x, 0)
            return False
        if ((self.x-self.r) < 0):
            self.premik(-x, 0)
            return False
        count = 0
        for ovira in ovire_list:
            if(self.col_krog(ovira) == True):
                count += 1
                if(count > 1):
                    self.premik(v[0], v[1])
                    self.premik(-x, -y)
                    return False
                v = [ovira.x - self.x, ovira.y - self.y]
                lenV = (v[0]**2 + v[1]**2)**1/2
                v[0] = v[0]/lenV
                v[1] = v[1]/lenV
                v[0] = v[0]*(ovira.r + self.r)
                v[1] = v[1]*(ovira.r + self.r)
                #print(v)

                #self.premik(-self.x + ovira.x + v[0], -self.y + ovira.y + v[1])
                self.premik(-v[0], -v[1])
        return True
                

    def movement(self, vx, vy):
        if(vx == 0 and vy == 0):
            return False
        if(vx != 0 and vy != 0):
            self.preveri_premik(self.speed*vx/2**(0.5), self.speed*vy/2**(0.5))
        else:
            self.preveri_premik(self.speed*vx, self.speed*vy)
        #self.update()
    """
def streljaj(self, x, y):
## global metki_list
## metki_list.append(Metek(self.canvas, self.x, self.y, 5, 350, 10, x, y, "black"))
## metki_list[-1].izris()
if "<Button-1>" in keys:
self.weapon.update(x, y)
"""
######################################################################################################################################################
class rldBar:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player
        self.izrisi = False
    
    def izris_frame(self):
        if(self.player.weapon.rld_t != None):
            self.frame_index = self.canvas.create_rectangle(self.player.x-(self.player.r*0.9), self.player.y-(self.player.r+15), self.player.x+(self.player.r*0.9), self.player.y-(self.player.r+5), outline = 'black', width = 2)
    def izris_rldbar(self):
        if(self.player.weapon.rld_t != None):
            self.rldbar_index = self.canvas.create_rectangle(self.player.x-(self.player.r*0.9), self.player.y-(self.player.r+15), (self.player.x+(self.player.r*0.9)) - self.player.r*1.8*(1 - (time.time() - self.player.weapon.rld_t)/self.player.weapon.rldt), self.player.y-(self.player.r+5), fill="#0077bb")

    def izris(self):
        self.izris_frame()
        self.izris_rldbar()

    def kill(self):
        try:
            self.canvas.delete(self.frame_index)
            self.canvas.delete(self.rldbar_index)
        except:
            pass
    
    def update(self):
        self.kill()
        self.izris()


######################################################################################################################### tukaj je to ################

class Weapon:
    #def __init__(self, canvas, player, dmg, rof, r, speed, mag, rldt):
    def __init__(self,dmg, rof, r, speed, mag, rldt, canvas, player, cluster = 1, spread = 0):
        #self.x, self.y = miska (ciljna destinacija)
        self.canvas = canvas
        self.player = player
        self.dmg = dmg
        self.rof = rof
        self.r = r
        self.speed = speed
        self.t = 0
        self.x = 0
        self.y = 0
        self.mag = mag
        self.max_mag = mag
        self.rld_t = None
        self.rldt = rldt
        self.cluster = cluster
        self.spread = spread

        
    def streljaj(self):
        global metki_list
        if(self.player.reloading == False):
            self.x -= 220
            for i in range(self.cluster):
                self.x += 20
                self.calc_spread()
                metki_list.append(Metek(self.canvas, self.player.x, self.player.y, self.r, self.speed, self.dmg, self.vx, self.vy, "black", playerr = self.player.r))
        for i in metki_list[-self.cluster:]:
            i.izris()
        #metki_list[-1].izris()
    def calc_spread(self):
        tx = abs(self.player.x - self.x)
        ty = abs(self.player.y - self.y)
        try:
            self.vx = -(tx/(self.player.x-self.x))*tx/((tx**2+ty**2)**(1/2))
            self.vy = -(ty/(self.player.y-self.y))*ty/((tx**2+ty**2)**(1/2))
        except ZeroDivisionError:
            print('ustrelil si tocno v sredino samega sebe')
            self.vx = 0
            self.vy = 0



            
        #R = 1
        #x = R*tg(spread/2)
        #return x
    
    def update(self):
        if self.mag > 0 and time.time() - self.t >= self.rof:
            self.x = mouseX
            self.y = mouseY
            self.t = time.time()
            self.streljaj()
            self.mag -= 1
    def rld(self):
        if time.time() - self.rld_t >= self.rldt:
            self.mag = self.max_mag
            self.rld_t = None
            self.player.reloading = False
    

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
    def __init__(self, canvas, x, y, r, speed, dmg, vx, vy, color, playerr = 35):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.dmg = dmg
        self.color = color
        self.playerr = playerr
        self.vx = vx
        self.vy = vy

        self.x += self.playerr * self.vx
        self.y += self.playerr * self.vy


        """
        tx = abs(self.x - destx)
        ty = abs(self.y - desty)
        try:
            self.vx = -(tx/(self.x-destx))*tx/((tx**2+ty**2)**(1/2))
            self.vy = -(ty/(self.y-desty))*ty/((tx**2+ty**2)**(1/2))
        except ZeroDivisionError:
            print('ustrelil si tocno v sredino samega sebe')
            self.vx = 0
            self.vy = 0
        #print("{0}, {1}\n".format(self.x, self.y))

        self.x += self.playerr * self.vx
        self.y += self.playerr * self.vy

        """
        

        #print("{0}, {1}\n".format(self.x, self.y))

        #print(self.vx, self.vy, abs(self.vx+self.vy))
        
        
        
        
    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, outline="black", width = 0)
    def update(self, t):
        #Ce se metek nikamor ne premika, ga izbrisi, drugace nam ko ustrelimo v sredino metki vedno ostanejo tam
        if(self.vx == 0 and self.vy == 0):
            self.kill()
            return 0
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
#'''
class HpBar:
    def __init__(self, canvas, zombij):
        self.canvas = canvas
        self.zombij = zombij
        self.izrisi = False
    
    def izris_frame(self):
        self.frame_index = self.canvas.create_rectangle(self.zombij.x-(self.zombij.r*0.9), self.zombij.y-(self.zombij.r+15), self.zombij.x+(self.zombij.r*0.9), self.zombij.y-(self.zombij.r+5), outline = 'black', width = 2)
    def izris_hpbar(self):
        self.hpbar_index = self.canvas.create_rectangle(self.zombij.x-(self.zombij.r*0.9), self.zombij.y-(self.zombij.r+15), (self.zombij.x+(self.zombij.r*0.9)) - self.zombij.r*1.8*(1 - (self.zombij.health/self.zombij.maxhp)), self.zombij.y-(self.zombij.r+5), fill="red")

    def izris(self):
        self.izris_frame()
        self.izris_hpbar()

    def kill(self):
        self.canvas.delete(self.frame_index)
        self.canvas.delete(self.hpbar_index)
    
    def update(self):
        self.kill()
        self.izris()

    
#????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        
class Zombij:
    def __init__(self, canvas, x, y, r, speed, health, dmg, frekvenca_napadanja):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.speed = speed
        self.maxhp = health
        self.health = health
        self.dmg = dmg
        self.vx = 0
        self.vy = 0
        self.hpBar = HpBar(self.canvas, self)
        self.hpBar.izris()
        self.jezen = False
        self.bo_udaril = True
        self.t = 0
        self.frekvenca_napadanja = frekvenca_napadanja
        


    def update(self, t):
        self.update_dest()
        self.napadi()
        self.col_ply()
        if(self.preveri_premik(self.vx*t*self.speed, self.vy*t*self.speed) == True):
            self.canvas.delete(self.index)
            self.izris()
            #if self.hp##################################################################################################
            self.hpBar.update()

    def izris(self):
        self.index = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill= ('#055505'), outline="black", width = 1)

    def napadi(self):
        if self.bo_udaril == False:
            if(time.time() - self.t >= self.frekvenca_napadanja):
                self.bo_udaril = True

    def col_ply(self):
        if(((self.x-ply.x)**2 + (self.y-ply.y)**2)**0.5 < self.r + ply.r):
            if self.bo_udaril == True:
                ply.ranjen(self.dmg)
                self.bo_udaril = False
                self.t = time.time()
        
    
    def ranjen(self, hp):
        self.health -= hp
        if(self.health <= 0):
            #print("Kill")
            self.kill()
        else:
            self.hpBar.update()
            
    def preveri_zivljenje(self):
        if(self.health() <= 0):
            self.kill()

    def kill(self):
        self.canvas.delete(self.index)
        zombij_list.remove(self)
        self.hpBar.kill()

    def premik(self, x, y):
        self.x += x
        self.y += y

    def zbudi_metek(self):
        for metek in metki_list:
            if ((((self.x-metek.x)**2+(self.y-metek.y)**2)**0.5)<300):
                return True

    def update_dest(self):
        if(self.jezen):
            try:
                tx = abs(self.x - ply.x)
                ty = abs(self.y - ply.y)
                self.vx = -(tx/(self.x-ply.x))*tx/((tx**2+ty**2)**(1/2))
                self.vy = -(ty/(self.y-ply.y))*ty/((tx**2+ty**2)**(1/2))
            except ZeroDivisionError:
                pass
        else:
            if (((((self.x-ply.x)**2+(self.y-ply.y)**2)**0.5)<300)or(self.zbudi_metek()==True)):
                self.jezen = True
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
    '''
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
'''
    def preveri_premik(self, x, y):
        self.premik(x, y)
        if ((self.y-self.r) < 0):
            self.premik(0, -y)
            return False
        if ((self.y+self.r) >=Y):
            self.premik(0, -y)
            return False
        if ((self.x+self.r) >= X):
            self.premik(-x, 0)
            return False
        if ((self.x-self.r) < 0):
            self.premik(-x, 0)
            return False
        count = 0
        for ovira in ovire_list:
            if(self.col_krog(ovira) == True):
                count += 1
                if(count > 1):
                    self.premik(v[0], v[1])
                    self.premik(-x, -y)
                    return False
                v = [ovira.x - self.x, ovira.y - self.y]
                lenV = (v[0]**2 + v[1]**2)**1/2
                v[0] = v[0]/lenV
                v[1] = v[1]/lenV
                v[0] = v[0]*(ovira.r + self.r)
                v[1] = v[1]*(ovira.r + self.r)
                #print(v)

                #self.premik(-self.x + ovira.x + v[0], -self.y + ovira.y + v[1])
                self.premik(-v[0], -v[1])
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

    for ply in player_list[:]:
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
        ply.update()

    for metek in metki_list[:]:
        metek.update(tmp)

    for zombij in zombij_list[:]:
        zombij.update(tmp)

    for ply in player_list[:]:
        ply.hpBar.update()
    
    root.after(1, update, t)

    if("Mouse1" in keys):
        ply.weapon.update()

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

#def mouse_input(event):
# print ("clicked at", event.x, event.y)
    #ply.streljaj(event.x, event.y)

def mousePress(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y

    if("Mouse1" not in keys):
        keys.append("Mouse1")

    #print(keys)

def mouseRelease(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y

    if("Mouse1" in keys):
        keys.remove("Mouse1")

    #print(keys)

def mouseUpdate(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    


hpbar_list = []
keys = []
player_list = []
ovire_list = []
zombij_list = []
metki_list = []
rldbar_list = []

mouseX = 0
mouseY = 0

nice_blue = "#00A2FF"
X=1000
Y=900
root = Tk()
canvas = Canvas(root, bg=('#807777'), width=X, height=Y)
canvas.pack()

#(self,dmg, rof, r, speed, mag, rldt, canvas = canvas, player = ply)

############# USTVARI IGRALCA ######################
ply = Player(canvas, 100, 100, 35, 300, 20, 20)

Uzi = Weapon(3, 0.05, 3, 350, 20, 1, canvas, ply)
DPistola = Weapon(150, 1, 4, 1000, 3, 3, canvas, ply)
Shotgun = Weapon(10, 0.5, 5, 200, 6, 1, canvas, ply, cluster = 10, spread = 60)


ply.weaponInit(Shotgun)
player_list.append(ply)
ply.izris()



#===============postavi okrogle ovire========================#

for i in range (10):
    ovira = Ovira_Krog(canvas, random.randint(150, X-100), random.randint(150, Y-100), random.randint(10, 50))
    ovire_list.append(ovira)
    ovira.izris()

#===============ustvari zombije==============================#

#self, canvas, x, y, r, speed, health, dmg)

for i in range(1):
    r = random.randint(10,50)
    zombij_list.append(Zombij(canvas, random.randint(r, X-r), random.randint(r, Y-r), r, random.randint(10,250), random.randint(10,100), 5, 3))
    zombij_list[-1].izris()

def spawn_zombij(event):
    r = random.randint(10,50)
    zombij_list.append(Zombij(canvas, random.randint(r, X-r), random.randint(r, Y-r), r, random.randint(10,250), random.randint(10,100), 5, 3))
    zombij_list[-1].izris()
def kilall(event):
    for i in zombij_list[:]:
        if ((((i.x-ply.x)**2+(i.y-ply.y)**2)**0.5)<300):
            i.kill()

def ugasni(event):
    root.quit()
    root.destroy()


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
canvas.bind("<ButtonPress-1>", mousePress)
canvas.bind("<ButtonRelease-1>", mouseRelease)
canvas.bind("<B1-Motion>", mouseUpdate)
root.bind_all("<space>", spawn_zombij)
root.bind_all("q", ugasni)
root.bind_all("<KeyPress>", keyPressHandler)
root.bind_all("<KeyRelease>", keyReleaseHandler)
root.bind_all("f", kilall)


update(time.time())

#canvas.bind("<Button-1>", xy)
#canvas.bind("<B1-Motion>", addLine)
#canvas.bind("A", delete)

root.mainloop()
