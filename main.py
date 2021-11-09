from tkinter import *
import random

tk = Tk()
tk.title("Футбол")
c = Canvas(tk, width =800, height = 600, bg = "green", cursor = "gumby" )
c.pack()

start = [- 1.5, 1.5]

class Balss():
    def __init__(self):
        self.x_poss = 740
        self.y_poss = 50
        self.wight = 50
        self.body = c.create_oval(self.x_poss,self.y_poss,self.x_poss + self.wight,self.y_poss + self.wight)
        self.x = random.choice(start)
        self.y = random.choice(start)

    def moving(self):
        c.move(self.body, self.x, self.y)
        self.position = c.coords(self.body)
        self.xl,self.yl, self.xr,self.yr = self.position
        if self.xl<0 or self.xr>800:
            self.x = -self.x
        if self.yl<0 or self.yr>600:
            self.y = -self.y

        c.after(10, self.moving)

enemy = Balss()
enemy.moving()
tk.mainloop()

