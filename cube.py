#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *


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

    def show(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        screen.fill((255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == 285 and event.mod == 256:
                        exit()
                    if event.key == K_r:
                        self.R()
                    if event.key == K_f:
                        self.F()
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

a.show()
