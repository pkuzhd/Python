#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import ttk

class cube():
    def __init__(self, cubelist):
        self.cube = cubelist
        self.color = {
                        1:[255, 0, 0],#红
                        2:[0, 0, 255],#蓝
                        3:[255, 255, 255],#白
                        4:[255, 100, 0],#橙
                        5:[0, 255, 0],#绿
                        6:[255, 255, 0],#黄
                    }
        self.play = {'R':self.R, 'F':self.F, "'":None, '2':None}
        self.w = 32.5
        self.h = 45
        self.p = 20
        #f, r, u, b, l, d
        #0, 1, 2, 3, 4, 5

    def polygonlist_f(self, x, y, i=400, j=300):
        p1 = ((x-3)*self.w+i       , (3-y)*self.h+(x-3)*self.p+j)
        p2 = ((x-3)*self.w+i       , (3-y)*self.h+(x-3)*self.p+j+self.h)
        p3 = ((x-3)*self.w+i-self.w, (3-y)*self.h+(x-3)*self.p+j+self.h-self.p)
        p4 = ((x-3)*self.w+i-self.w, (3-y)*self.h+(x-3)*self.p+j-self.p)
        return [p1, p2, p3, p4]

    def polygonlist_r(self, x, y, i=400, j=300):
        p1 = ((x-1)*self.w+i       , (3-y)*self.h+(1-x)*self.p+j)
        p2 = ((x-1)*self.w+i+self.w, (3-y)*self.h+(1-x)*self.p+j-self.p)
        p3 = ((x-1)*self.w+i+self.w, (3-y)*self.h+(1-x)*self.p+j+self.h-self.p)
        p4 = ((x-1)*self.w+i       , (3-y)*self.h+(1-x)*self.p+j+self.h)
        return [p1, p2, p3, p4]

    def polygonlist_u(self, x, y, i=400, j=300):
        p1 = ((x-3)*self.w+(y-1)*self.w+i       , (x-3)*self.p+(1-y)*self.p+j)
        p2 = ((x-3)*self.w+(y-1)*self.w+i+self.w, (x-3)*self.p+(1-y)*self.p+j-self.p)
        p3 = ((x-3)*self.w+(y-1)*self.w+i       , (x-3)*self.p+(1-y)*self.p+j-self.p*2)
        p4 = ((x-3)*self.w+(y-1)*self.w+i-self.w, (x-3)*self.p+(1-y)*self.p+j-self.p)
        return [p1, p2, p3, p4]

    def R(self):
        temp = self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2]
        self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2] = self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0]
        self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0] = self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0]
        self.cube[3][2][2], self.cube[3][2][1], self.cube[3][2][0] = self.cube[2][2][0], self.cube[2][2][1], self.cube[2][2][2]
        self.cube[2][2][0], self.cube[2][2][1], self.cube[2][2][2] = temp
        temp = self.cube[1][0][0]
        self.cube[1][0][0] = self.cube[1][2][0]
        self.cube[1][2][0] = self.cube[1][2][2]
        self.cube[1][2][2] = self.cube[1][0][2]
        self.cube[1][0][2] = temp
        temp = self.cube[1][0][1]
        self.cube[1][0][1] = self.cube[1][1][0]
        self.cube[1][1][0] = self.cube[1][2][1]
        self.cube[1][2][1] = self.cube[1][1][2]
        self.cube[1][1][2] = temp
    def R_(self):
        R()
        R()
        R()
    def F(self):
        temp = self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0]
        self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0] = self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2]
        self.cube[4][0][0], self.cube[4][0][1], self.cube[4][0][2] = self.cube[5][2][0], self.cube[5][1][0], self.cube[5][0][0]
        self.cube[5][2][0], self.cube[5][1][0], self.cube[5][0][0] = self.cube[1][0][2], self.cube[1][0][1], self.cube[1][0][0]
        self.cube[1][0][2], self.cube[1][0][1], self.cube[1][0][0] = temp
        temp = self.cube[0][0][0]
        self.cube[0][0][0] = self.cube[0][2][0]
        self.cube[0][2][0] = self.cube[0][2][2]
        self.cube[0][2][2] = self.cube[0][0][2]
        self.cube[0][0][2] = temp
        temp = self.cube[0][0][1]
        self.cube[0][0][1] = self.cube[0][1][0]
        self.cube[0][1][0] = self.cube[0][2][1]
        self.cube[0][2][1] = self.cube[0][1][2]
        self.cube[0][1][2] = temp
    def F_(self):
        F()
        F()
        F()

    def run(self, strings):
        t1 = None
        t2 = None
        for i in strings:
            if i in self.play:
                if t1 == None:
                    t1 = i
                elif t2 == None:
                    t2 = i
                    if t2 == "'":
                        self.play[t1]()
                        self.play[t1]()
                        self.play[t1]()
                        t1 = None
                        t2 = None
                    elif t2 == '2':
                        self.play[t1]()
                        self.play[t1]()
                        t1 = None
                        t2 = None
                    else:
                        self.play[t1]()
                        t1 = t2
                        t2 = None
        if t1 != None:
            self.play[t1]()

    def show(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        screen.fill((255, 255, 255))
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         exit()
        #     if event.type == KEYDOWN:
        #         if event.key == 285 and event.mod == 256:
        #             exit()
        #         if event.key == K_r:
        #             self.R()
        #         if event.key == K_f:
        #             self.F()
        for i in range(1, 4):
            for j in range(1, 4):
                pygame.draw.polygon(screen, self.color[self.cube[0][i-1][j-1]], self.polygonlist_f(i, j), 0)
                pygame.draw.polygon(screen, self.color[self.cube[1][i-1][j-1]], self.polygonlist_r(i, j), 0)
                pygame.draw.polygon(screen, self.color[self.cube[2][i-1][j-1]], self.polygonlist_u(i, j), 0)
                pygame.draw.aalines(screen, [0, 0, 0], True, self.polygonlist_f(i, j), 1)
                pygame.draw.aalines(screen, [0, 0, 0], True, self.polygonlist_r(i, j), 1)
                pygame.draw.aalines(screen, [0, 0, 0], True, self.polygonlist_u(i, j), 1)
                pygame.draw.polygon(screen, self.color[self.cube[3][i-1][j-1]], self.polygonlist_f(i, j, 400+7*self.w, 300-7*self.p), 0)
                pygame.draw.polygon(screen, self.color[self.cube[4][i-1][j-1]], self.polygonlist_r(i, j, 400-7*self.w, 300-7*self.p), 0)
                pygame.draw.polygon(screen, self.color[self.cube[5][i-1][j-1]], self.polygonlist_u(i, j, 400, 300+6*self.h), 0)
                pygame.draw.aalines(screen, [0, 0, 0], True, self.polygonlist_f(i, j, 400+7*self.w, 300-7*self.p), 1)
                pygame.draw.aalines(screen, [0, 0, 0], True, self.polygonlist_r(i, j, 400-7*self.w, 300-7*self.p), 1)
                pygame.draw.aalines(screen, [0, 0, 0], True, self.polygonlist_u(i, j, 400, 300+6*self.h), 1)
        pygame.display.update()

a = cube([
        [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
        ],
        [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
        ],
        [
        [3, 3, 3],
        [3, 3, 3],
        [3, 3, 3]
        ],
        [
        [4, 4, 4],
        [4, 4, 4],
        [4, 4, 4]
        ],
        [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
        ],
        [
        [6, 6, 6],
        [6, 6, 6],
        [6, 6, 6]
        ],
    ])


def play(*args):
    value = str(feet.get())
    a.run(value)
    a.show()

root = Tk()
root.title("cube")
a.show()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=30, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="play", command=play).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="命令").grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', play)

root.mainloop()









# from tkinter import *
# from tkinter import ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass
# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)

# feet = StringVar()
# meters = StringVar()

# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind('<Return>', calculate)

# root.mainloop()
