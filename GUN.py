from tkinter import *
from random import randrange as rnd, choice
root = Tk()
root.geometry('900x600')

canv = Canvas(root, bg='black')
canv.pack(fill=BOTH, expand=1)
root.resizable(width=False,height=False)
count = 0
colors = ['salmon', 'orange', 'yellow', 'greenyellow', 'plum', 'pink', 'lightblue','purple', 'lightgreen', 'black', 'white']
class Bomb():
    def __init__(self, coord, vel1, vel2, rad=10 ):
        self.color = 'white'
        self.coord = coord
        self.vel1 = vel1
        self.vel2 = vel2
        self.rad = rad
        self.is_alive = True
    def draw_bomb(self, screen):
        canv.create_oval(self.coord[0] - self.rad, self.coord[1] - self.rad, self.coord[0] + self.rad, self.coord[1] + self.rad, fill=colors, width=0)
        canv.create_polygon(self.coord[0] + 2 * self.rad // 3, self.coord[1] - self.rad, self.coord[0] + self.rad, self.coord[1] - 2 * self.rad // 3, self.coord[0] + 2 * self.rad // 3, self.coord[1] - self.rad // 3, self.coord[0] + self.rad // 3, self.coord[1] - 2 * self.rad // 3, fill='black', width=0)
        canv.create_line(self.coord[0], self.coord[1], self.coord[0] + self.rad, self.coord[1] - self.rad, self.coord[0] + 4 * self.rad // 3, self.coord[1] - self.rad, self.coord[0] + 7 * self.rad // 6, self.coord[1] - self.rad // 3, self.coord[0] + 4 * self.rad // 3, self.coord[1],
                         smooth=1, width=2)

    def move(self, t_step=1., g=2.):
        for i in range(2):
            self.coord[i] += int(self.vel1[i] * t_step)
        for i in range(2):
            self.coord[i + 2] += int(self.vel2[i] * t_step)
        if self.coord[0] <= 0 or self.coord[3] <= 0:
            self.is_alive = False
class ball():
    def __init__(self,coord,vel1,vel2,rad):
        self.color = colors
        self.vel1 = vel1
        self.vel2 = vel2
        self.rad = rad
        self.is_alive = True
    def draw_ball (self,):
        canv.create_oval(self,)







root.mainloop()