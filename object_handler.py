from sprite_object import *
from npc import *
import random
from settings import*


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resorces/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #Sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game, path = self.anim_sprite_path + 'red_light/0.png', pos = (14.5, 17.5)))
        add_sprite(AnimatedSprite(game, path = self.anim_sprite_path + 'red_light/0.png', pos = (16.5,17.5)))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos= (5.5, 27.5)))

        #NPC map
        s_map = self.game.map.mini_map
        a,b = PLAYER_POS
        add_npc(NPC(game))
        add_npc(NPC(game, pos = (1.5, 1.5)))

        #Random entities
        for j,row in enumerate(s_map):
            for i, value in enumerate(row):
                if not value:
                    if (not(abs(a-i) < 5) or not (abs(b-j) < 5)):# and not (s_map[j+1][i+1]) :
                        if random.randint(1,99) < 10:
                            add_npc(NPC(game, pos = (i+0.5, j+0.5)))
        
        #add_npc(NPC(game, pos = (10.5, 21.5)))
        #add_npc(NPC(game, pos = (3.5, 3.5)))
        #add_npc(NPC(game, pos = (3.5, 5.5)))
        #add_npc(NPC(game, pos = (3.5, 7.5)))
        #add_npc(NPC(game, pos = (3.5, 9.5)))
        #add_npc(NPC(game, pos = (3.5, 13.5)))
        #add_npc(NPC(game, pos = (20.5, 4.5)))
        #add_npc(NPC(game, pos = (20.5, 6.5)))
        #add_npc(NPC(game, pos = (15.5, 18.5)))
        #add_npc(NPC(game, pos = (16.5, 18.5)))
        #add_npc(NPC(game, pos = (17.5, 18.5)))
        #add_npc(NPC(game, pos = (18.5, 18.5)))
        #add_npc(NPC(game, pos = (19.5, 18.5)))
        #add_npc(NPC(game, pos = (15.5, 19.5)))
        #add_npc(NPC(game, pos = (17.5, 19.5)))
        #add_npc(NPC(game, pos = (29.5, 23.5)))
        #add_npc(NPC(game, pos = (29.5, 24.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self,npc):
        self.npc_list.append(npc)

    
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
