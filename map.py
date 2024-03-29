import pygame as pg
from settings import *
from rand_map import *

_ = False



mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,3,3,3,_,_,_,_,2,_,_,_,_,_,_,_,2,1,1,1,1,1,1,1,1,1,1,2,_,_,1],
    [1,_,_,_,3,_,_,_,_,2,2,2,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,2,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,2,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,3,_,1,1,_,2,_,_,_,3,3,4,3,3,_,_,2,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,3,_,_,_,_,2,_,_,_,_,_,1,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,1,_,_,_,_,3,1,_,_,1,2,_,_,_,_,_,1,_,_,_,_,1,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,3,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,1,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,3,_,1,1,_,2,1,1,1,1,1,1,1,1,1,1,1,_,_,1],
    [1,_,_,_,2,2,2,2,2,2,2,2,2,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,2,_,_,_,_,1,1,1,2,2,2,2,1,1,1],
    [1,_,_,_,_,_,_,_,2,_,_,_,1,1,1,1,1,1,1,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,1,_,_,2,_,_,_,1,_,_,_,_,_,1,_,_,1,_,_,_,_,_,_,3,_,_,1],
    [1,_,_,_,_,1,_,_,2,_,_,_,1,_,2,_,2,_,1,2,2,1,_,_,3,3,3,3,3,_,_,1],
    [1,_,_,_,_,1,_,_,_,_,_,_,_,_,2,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,_,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,2,2,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,2,2,_,_,_,_,_,_,1,1,1,1,1,1,1,_,_,_,_,_,1],
    [1,_,_,_,3,_,_,_,_,_,_,_,2,2,2,2,3,_,_,1,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,3,_,_,_,_,_,_,_,_,_,_,_,3,_,_,1,_,_,_,_,_,_,3,3,3,_,_,1],
    [1,_,_,_,3,_,_,_,_,_,_,2,_,_,_,_,3,_,_,1,_,_,_,_,_,_,3,_,_,_,_,1],
    [1,_,_,_,3,_,_,_,_,_,_,2,_,_,_,_,3,1,1,1,_,_,_,2,_,_,3,_,_,_,_,1],
    [1,_,_,_,3,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,3,3,3,_,_,1],
    [1,_,2,2,4,2,2,2,3,3,3,2,3,3,_,_,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,1],
    [1,_,2,_,_,_,2,_,_,_,_,_,_,3,1,_,_,_,_,_,_,_,_,2,_,_,_,1,_,_,_,1],
    [1,_,2,_,_,_,2,_,_,_,_,_,_,_,3,3,3,3,3,3,_,_,_,2,_,_,_,1,_,_,_,1],
    [1,_,2,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Map:
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map #gen_map() #mini_map #new_map()
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value
    
    def draw(self):
        [pg.draw.rect(self.game.screen, 'blue', (pos[0]*MAP_SCALE, pos[1]*MAP_SCALE,MAP_SCALE,MAP_SCALE),2)
        for pos in self.world_map]